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
