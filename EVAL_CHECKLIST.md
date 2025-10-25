# Kasparro Applied AI Engineer — Evaluation Checklist

This checklist ensures that the Agentic Facebook Performance Analyst assignment meets all requirements.

## Repository

- [ ] Repository name format: `kasparro-agentic-fb-analyst-<firstname-lastname>`
- [ ] README.md with setup instructions, CLI commands, sample outputs, and v1.0 release tag
- [ ] Config file (`config/config.yaml`) exists with thresholds, seeds, and paths

## Agents

- [ ] Planner Agent is modular and decomposes user queries into subtasks
- [ ] Data Agent loads CSV dataset and summarizes metrics
- [ ] Insight Agent generates structured hypotheses with confidence
- [ ] Evaluator Agent validates hypotheses quantitatively
- [ ] Creative Generator produces actionable recommendations for low-CTR campaigns

## Prompts

- [ ] All prompts stored as separate `.md` files in `prompts/`
- [ ] Prompts are structured for reasoning (Think → Analyze → Conclude)
- [ ] Reflection/retry logic included for low-confidence results

## Reports & Logs

- [ ] `reports/` folder contains `report.md`, `insights.json`, `creatives.json`
- [ ] `logs/` folder exists with JSON traces or Langfuse evidence

## Testing & Validation

- [ ] Evaluator tests exist in `tests/` and pass successfully
- [ ] Randomness is seeded for reproducibility
- [ ] Small sample dataset works for quick testing

## Git Hygiene

- [ ] At least 3 commits(more than 3 commits present)
- [ ] v1.0 release tag present
- [ ] PR titled `self-review` describing design choices and trade-offs( check SELF_REVIEW.md file )
