Insight Agent
-------------
Input: data_summary

Output: JSON list of candidate hypotheses, each with:
{
 "hypothesis_id": "H1",
 "statement": "...",
 "rationale": "...",
 "expected_signals": ["ctr_drop", "impression_spike", "audience_overlap"],
 "confidence": 0.0
}

Guidance: use temporal comparisons (last 7 days vs previous 28 days), segment by campaign/adset/creative_type.
