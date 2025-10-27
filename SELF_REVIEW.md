# Self-Review: Kasparro Agentic FB Analyst

## Design Decisions
1. **Planner Agent** — Decomposes user query into structured subtasks for modular workflow.
2. **Data Agent** — Loads CSV, summarizes performance metrics for further analysis.
3. **Insight Agent** — Generates structured hypotheses in JSON format.
4. **Evaluator Agent** — Validates hypotheses quantitatively using thresholds in `config.yaml`.
5. **Creative Generator** — Suggests grounded creative variants for low-CTR campaigns.

---

## Trade-offs
- Focused on a **simple attention mechanism** for explainability and stability.
- Used **heuristics for low CTR** detection instead of full model-based prediction due to timeline constraints.
- No UI or API interface — only CLI for reproducibility.

---

## Observability
- Logs stored in:
  - `reports/insights.json`
  - `reports/evaluations.json`
  - `reports/creatives.json`
  - `reports/observability/logs/run_*.json`
- Added **reflection logging** to `reports/reflection_log.json` for replan tracking.

---

## Reproducibility
- Random seeds and thresholds stored in `config/config.yaml`.
- Deterministic output generation.
- Dependencies pinned in `requirements.txt`.

---

## Final Reflection (New)
After full pipeline execution, **reflection logic** analyzes evaluator confidence scores.  
- If any hypothesis falls below `confidence_min` (default 0.6), a **replan suggestion** is logged.  
- This mechanism enables **self-corrective loops**, preparing the architecture for future adaptive planning integration.

*Next iteration*: connect reflection output → planner input for automatic hypothesis refinement.

---

### Example Trigger
If Evaluator returns:
```json
{"hypothesis_id": "H_lowROAS", "confidence": 0.52}
