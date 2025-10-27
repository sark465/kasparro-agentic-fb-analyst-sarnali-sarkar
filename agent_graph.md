# Agent Graph: Kasparro Agentic FB Analyst

## Overview
This system uses a modular, multi-agent framework for marketing analytics.  
It performs **data summarization**, **insight generation**, **evaluation**, and **creative ideation**, with a new **reflection/replan** loop added for adaptive learning.

---

## 🧩 Agents and Roles

| Agent | Input | Output | Description |
|--------|--------|---------|-------------|
| **Planner Agent** | User query | Subtask list | Decomposes query into subtasks |
| **Data Agent** | CSV data | Summaries (CTR, ROAS, spend) | Loads, cleans, and aggregates data |
| **Insight Agent** | Data summary | Hypotheses (JSON) | Generates structured hypotheses |
| **Evaluator Agent** | Hypotheses, Data | Evaluation metrics, Confidence | Quantitatively validates hypotheses |
| **Creative Generator** | Low-CTR campaigns | Grounded creative ideas | Suggests data-informed ad messages |
| **Reflection Module (New)** | Evaluations | Replan triggers | Logs low-confidence cases for next planning cycle |

--- 


1. ## Data Flow Diagram

```text
         ┌────────────┐
         │  User Query │
         └─────┬──────┘
               │
               ▼
         ┌────────────┐
         │  Planner    │
         └─────┬──────┘
               │
               ▼
         ┌────────────┐
         │ Data Agent │
         └─────┬──────┘
               │
               ▼
         ┌──────────────┐
         │ Insight Agent│
         └─────┬────────┘
               │
               ▼
         ┌──────────────┐
         │ Evaluator    │
         └─────┬────────┘
               │
      ┌────────┴─────────┐
      ▼                  ▼
┌──────────────┐    ┌───────────────┐
│ Creative Gen │    │ reports/      │
│              │    │ insights.json │
│creatives.json│    │ report.md     │
└──────────────┘    └───────────────┘

2.** Key Highlights:**

## Agentic Architecture
- Planner Agent decomposes user queries into structured subtasks.
- Data Agent handles CSV loading, summarization, and basic aggregations.
- Insight Agent generates hypotheses with confidence scores.
- Evaluator Agent validates hypotheses quantitatively with simple thresholds.
- Creative Generator suggests new creative messages for low-CTR campaigns.

## Design Decisions & Tradeoffs
- **Separation of Concerns:** Each agent focuses on a specific role to maintain modularity.
- **Data Summarization:** Only summaries passed to Insight Agent instead of full CSV to reduce overhead.
- **Confidence & Validation:** Simplified numeric thresholds used for hypothesis evaluation for clarity and reproducibility.
- **Creative Generation:** Variants are grounded in existing campaign messages; no external model required to keep the system lightweight.
- **Logging & Observability:** JSON run logs stored in `logs/` for traceability.

## Configuration & Reproducibility
- `config/config.yaml` defines thresholds, seeds, and output paths.
- Randomness is seeded for reproducible results.
- Small sample dataset provided for quick testing.

## Prompts & Templates
- All prompts stored as separate `.md` files in `prompts/` for reusability and maintainability.

## Outputs
- `reports/report.md` — human-readable summary.
- `reports/insights.json` — structured hypotheses and evaluation.
- `reports/creatives.json` — recommended creative messages.

## Remaining Notes
- Evaluator tests (`tests/test_evaluator.py`) should be verified to pass before merging.

This PR ensures full transparency of design choices, implementation reasoning, and project reproducibility for version 1.0.

3. **Notes**

a. Each agent communicates via structured JSON outputs, not raw CSV.

b. Planner ensures task order and conditional execution.

c. Evaluator uses thresholds defined in config/config.yaml for confidence scoring.

d. Creative Generator leverages sample messages from low-CTR campaigns to produce actionable recommendations.