# Creative Improvement Generator
------------------------------

## Input:
- `low_ctr_campaigns` (list of campaigns with CTR < threshold)
- `sample_creative_messages` (existing ad copy, headlines, and CTAs)

## Output JSON Schema
```json
[
  {
    "campaign_name": "string",
    "creative_recommendations": [
      {
        "headline": "string",
        "body": "string",
        "cta": "string",
        "rationale": "string"
      }
    ]
  }
]
