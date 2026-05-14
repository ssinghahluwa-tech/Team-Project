import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from builds import build4_rag_router_agent_streamlit as backend

st.set_page_config(page_title="Build4 RAG Router Agent", layout="wide")

st.title("Build4 RAG Router Agent")

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.header("Setup")

uploaded_file = st.sidebar.file_uploader("Upload CSV dataset", type=["csv"])
report_dir = st.sidebar.text_input("Report directory", "reports")
knowledge_dir = st.sidebar.text_input("Knowledge directory", "knowledge")

if "agent" not in st.session_state:
    st.session_state.agent = None

if st.sidebar.button("Initialize Agent"):
    if uploaded_file is None:
        st.sidebar.error("Please upload a CSV file first.")
    else:
        temp_path = f"data/{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.session_state.agent = backend.initialize_build4_backend(
            data_path=temp_path,
            report_dir=report_dir,
            knowledge_dir=knowledge_dir,
            tags=["streamlit", "build4"],
        )

        st.sidebar.success("Agent initialized successfully.")

if st.session_state.agent is None:
    st.warning("Upload a CSV file and click Initialize Agent to begin.")
    st.stop()

agent = st.session_state.agent

# -----------------------
# DATASET INFO
# -----------------------
st.subheader("Dataset Schema")
st.text(agent["schema_text"])

st.subheader("Dataset Preview")
st.dataframe(agent["df"].head())

# -----------------------
# TABS
# -----------------------
tab1, tab2, tab3, tab4 = st.tabs(["Ask", "Tool", "Code", "Run"])

# -----------------------
# ASK TAB
# -----------------------
with tab1:
    st.header("Ask Router")
    ask_request = st.text_area("Enter a question or task:", key="ask_request")

    if st.button("Run Router"):
        result = backend.ui_run_router(agent, ask_request)
        st.session_state.last_router_result = result

        st.subheader("Router Decision")
        st.json(result["plan"])

        if result["plan"].get("note"):
            st.subheader("Answer")
            st.write(result["plan"]["note"])

# -----------------------
# TOOL TAB
# -----------------------
with tab2:
    st.header("Tool Mode")
    tool_request = st.text_area("Enter a tool request:", key="tool_request")

    if st.button("Plan Tool"):
        tool_plan = backend.ui_plan_tool(agent, tool_request)
        st.session_state.last_tool_plan = tool_plan

        st.subheader("Tool Plan")
        st.json(tool_plan["plan"])

    if "last_tool_plan" in st.session_state:
        if st.button("Approve and Run Tool"):
            tool_output = backend.ui_run_tool_from_plan(
                agent,
                tool_request,
                st.session_state.last_tool_plan["plan"],
            )

            if "error" in tool_output:
                st.error(tool_output["error"])
            else:
                st.subheader("Tool Used")
                st.write(tool_output["tool"])

                st.subheader("Summary")
                st.markdown(tool_output["summary"].replace("\n", "\n\n"))

                st.subheader("Raw Output")
                with st.expander("See raw tool output"):
                    st.text(tool_output["text"])

                if tool_output.get("artifacts"):
                    st.subheader("Artifacts")
                    st.write(tool_output["artifacts"])

# -----------------------
# CODE TAB
# -----------------------
with tab3:
    st.header("Code Generation")
    code_request = st.text_area("Enter a code generation request:", key="code_request")

    if st.button("Generate Code"):
        generated = backend.ui_run_codegen(agent, code_request)
        st.session_state.generated_code = generated

        st.subheader("Plan")
        st.markdown(generated.get("plan") or "No plan found.")

        if generated.get("code"):
            st.subheader("Generated Code")
            st.code(generated["code"], language="python")
        else:
            st.warning("No Python code block was generated.")
            with st.expander("See raw model output"):
                st.text(generated.get("raw", ""))

    if "generated_code" in st.session_state:
        if st.button("Approve and Save Code"):
            save_result = backend.ui_save_generated_code(
                agent,
                st.session_state.generated_code["code"],
            )

            if "error" in save_result:
                st.error(save_result["error"])
            else:
                st.session_state.saved_code_path = save_result["saved_path"]
                st.success(f"Code saved to {save_result['saved_path']}")

# -----------------------
# RUN TAB
# -----------------------
with tab4:
    st.header("Run Saved Code")

    if "saved_code_path" not in st.session_state:
        st.info("Generate and save code first.")
    else:
        st.write(f"Saved script: {st.session_state.saved_code_path}")

        if st.button("Run Saved Code"):
            result = backend.ui_run_saved_code(agent)

            st.subheader("Return Code")
            st.write(result["returncode"])

            st.subheader("STDOUT")
            st.text(result["stdout"])

            st.subheader("STDERR")
            st.text(result["stderr"])