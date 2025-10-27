
---

## 🧩 `planner_prompt.md`
```markdown
# Planner Agent
--------------

## Input:
- `user_query` (string)
- `data_summary` (dict containing dataset insights)

## Output JSON Schema
```json
{
  "tasks": [
    {"name": "load_data", "args": {}},
    {"name": "summarize_data", "args": {}},
    {"name": "generate_hypotheses", "args": {}},
    {"name": "validate_hypotheses", "args": {}},
    {"name": "generate_creatives", "args": {}}
  ]
}
