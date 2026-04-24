from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any

import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings


def build_rag_chunks(knowledge_dir: Path, chunk_size: int = 1000, overlap: int = 200):
    chunks = []

    for file_path in knowledge_dir.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append(
                {
                    "source": str(file_path),
                    "text": chunk_text,
                }
            )

            start += chunk_size - overlap

    return chunks


def build_faiss_index(chunks, embedding_model: str):
    embeddings = OpenAIEmbeddings(model=embedding_model)

    texts = [chunk["text"] for chunk in chunks]
    vectors = embeddings.embed_documents(texts)

    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    return index, vectors


def save_faiss_index(
    knowledge_dir: Path,
    index,
    chunks,
    embedding_model: str,
):
    index_path = knowledge_dir / "rag_faiss.index"
    meta_path = knowledge_dir / "rag_chunks.pkl"

    faiss.write_index(index, str(index_path))

    with open(meta_path, "wb") as f:
        pickle.dump(
            {
                "chunks": chunks,
                "embedding_model": embedding_model,
            },
            f,
        )

    return index_path, meta_path


def load_faiss_index(knowledge_dir: Path):
    index_path = Path(knowledge_dir) / "rag_faiss.index"
    meta_path = Path(knowledge_dir) / "rag_chunks.pkl"

    if not index_path.exists():
        raise FileNotFoundError(f"FAISS index not found: {index_path}")
    if not meta_path.exists():
        raise FileNotFoundError(f"Chunk metadata not found: {meta_path}")

    index = faiss.read_index(str(index_path))

    with open(meta_path, "rb") as f:
        meta = pickle.load(f)

    chunks = meta["chunks"]
    embedding_model = meta["embedding_model"]

    return index, chunks, embedding_model


def retrieve_chunks(
    query: str,
    index,
    chunks,
    k: int,
    embedding_model: str,
):
    embeddings = OpenAIEmbeddings(model=embedding_model)
    qvec = embeddings.embed_query(query)

    distances, indices = index.search(
        np.array([qvec]).astype("float32"),
        k,
    )

    results = []
    for idx in indices[0]:
        if idx < 0 or idx >= len(chunks):
            continue
        results.append(chunks[idx])

    return results


def format_rag_context(results) -> str:
    if not results:
        return "No relevant retrieved context."

    formatted = []
    for i, chunk in enumerate(results, start=1):
        source = chunk.get("source", "unknown")
        text = chunk.get("text", "")
        formatted.append(f"[Chunk {i}] Source: {source}\n{text}")

    return "\n\n".join(formatted)