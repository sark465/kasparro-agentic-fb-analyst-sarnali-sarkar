# Agent Graph: Kasparro Agentic FB Analyst

## Overview
The system is designed as a multi-agent architecture to analyze Facebook Ads performance, generate insights, validate hypotheses, and recommend new creative messages for low-CTR campaigns.  

## Agents and Roles

1. **Planner Agent**
   - **Input:** User query (e.g., "Analyze ROAS drop in last 7 days")
   - **Output:** Decomposed subtasks for other agents
   - **Role:** Organizes workflow and ensures structured analysis

2. **Data Agent**
   - **Input:** CSV dataset
   - **Output:** Data summaries (metrics, CTR, ROAS, campaign stats)
   - **Role:** Loads data, computes key metrics, prepares summary for Insight Agent

3. **Insight Agent**
   - **Input:** Data summary from Data Agent
   - **Output:** Hypotheses explaining observed patterns
   - **Role:** Generates structured, JSON-formatted hypotheses

4. **Evaluator Agent**
   - **Input:** Hypotheses from Insight Agent, raw data from Data Agent
   - **Output:** Quantitative evaluation of hypotheses (confidence scores)
   - **Role:** Validates hypotheses using thresholds in `config.yaml`

5. **Creative Generator**
   - **Input:** Low-CTR campaigns identified from Evaluator output
   - **Output:** Suggested creative messages (headlines, CTAs, copy)
   - **Role:** Provides actionable recommendations to improve ad performance

---

6. ## Data Flow Diagram

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

7. **Notes**

a. Each agent communicates via structured JSON outputs, not raw CSV.

b. Planner ensures task order and conditional execution.

c. Evaluator uses thresholds defined in config/config.yaml for confidence scoring.

d. Creative Generator leverages sample messages from low-CTR campaigns to produce actionable recommendations.