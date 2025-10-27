# Insight Agent Prompt

## Input
`data_summary` — aggregate and per-campaign metrics

## Output JSON Schema
```json
{
  "hypothesis_id": "string",
  "statement": "string",
  "rationale": "string",
  "expected_signals": ["string"],
  "confidence": "float (0-1)"
}