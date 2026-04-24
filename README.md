# Build4 RAG Router Agent

Name: Sumer Ahluwalia  
Course: QAC387  
Assignment: Build4 – RAG Router Agent  

---

## Purpose of the Application

This application is a Human-in-the-Loop (HITL) data analysis agent built using LangChain and an OpenAI LLM.

It allows users to interact with a dataset using natural language and automatically:

- Answer conceptual questions using Retrieval-Augmented Generation (RAG) with external knowledge documents  
- Route analysis tasks to predefined tools  
- Generate Python code for custom analyses  
- Require human approval before executing any code  
- Produce outputs, visualizations, and summaries  

The goal is to create a safe, flexible, and interpretable data analysis assistant.

---

## Instructions for Using the Application

### 1. Build the RAG Index (run once)

From the project root:

    PYTHONPATH=. python3 builds/build_rag_index.py --knowledge_dir knowledge

---

### 2. Run the Build4 Agent

From the project root:

    PYTHONPATH=. python3 builds/build4_rag_router_agent_faiss.py \
      --data data/McDonalds_Financial_Statements_Monthly_2005-2024.csv \
      --report_dir reports \
      --knowledge_dir knowledge \
      --tags build4 \
      --memory

---

### 3. Interact with the Agent

Use the CLI commands:

- ask <question> → Router decides (tool / codegen / RAG answer)  
- tool <request> → Force tool execution  
- code <request> → Generate Python code  
- run → Execute approved code  
- schema → View dataset structure  
- suggest <question> → Get analysis ideas  
- exit → Quit  

---

### Example Usage

- ask what does this dataset measure → Uses RAG  
- ask summarize numeric columns → Uses tools  
- ask plot earnings by P/E ratio → Uses codegen  

---

## Cautions for Using the Application

- All generated code must be manually approved before execution (HITL safeguard)  
- RAG responses depend on the quality of knowledge documents  
- The model may generate incorrect or inefficient code for complex tasks  
- Tool selection may not always be optimal for ambiguous requests  
- Langfuse tracing requires API keys; otherwise tracing will be disabled  
- Outputs should always be reviewed before drawing conclusions  

---

## Conclusion

This application successfully integrates:

- LangChain-based LLM interaction  
- Tool routing and code generation  
- Human-in-the-loop approval  
- RAG for contextual question answering  

It provides a robust and flexible framework for dataset exploration and analysis.










# Build3 HITL Router Agent

Name: Sumer Ahluwalia
Course: QAC387
Assignment: Build3 – HITL Router Agent

---

## Overview

This project implements a Human-in-the-Loop (HITL) data analysis agent using LangChain.
The agent routes user requests to either predefined Build0 tools or LLM-generated Python code.

The system ensures that all actions (tool execution or code execution) require human approval before running.

---

## Features

* Tool routing (automatic selection of Build0 tools)
* Code generation using LLM
* Human approval before execution (HITL)
* Custom tool: `grouped_summary`
* Artifact saving (outputs and figures)
* CLI-based interaction

---

## How to Run

```bash
python builds/build3_hitl_router_agent.py \
  --data data/McDonalds_Financial_Statements_Monthly_2005-2024.csv \
  --report_dir reports \
  --tags build3 \
  --memory
```

---

## Commands

* `suggest <question>` → Generate research ideas based on dataset schema
* `ask <request>` → Router decides tool vs codegen (HITL)
* `tool <request>` → Force tool execution (HITL)
* `code <request>` → Generate Python script (HITL)
* `run` → Execute last approved script
* `schema` → View dataset schema
* `help` → List available commands
* `exit` → Quit the agent

---

## Custom Tool

### grouped_summary

This custom tool performs grouped aggregation on a numeric column by a categorical column.

**Functionality:**

* Groups data by a specified column (`group_col`)
* Computes summary statistics for a numeric column (`value_col`)
* Outputs include:

  * count
  * mean
  * median
  * minimum
  * maximum

This tool demonstrates successful integration into:

* tool registry (`tools.py`)
* router decision-making
* HITL execution workflow

---

## Outputs

* Tool outputs: `reports/tool_outputs/`
* Figures: `reports/tool_figures/`
* Generated code: `reports/build3_generated_analysis.py`
* Execution logs: `reports/run_log.txt`

---

## Conclusion

The Build3 agent successfully demonstrates:

* Tool routing
* Human-in-the-loop approval
* Code generation and execution
* Custom tool integration

All required functionalities were implemented and tested with both success and failure cases documented.
