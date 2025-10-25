import numpy as np
import pandas as pd
from typing import Dict

def evaluate_hypothesis(hypo: Dict, df: pd.DataFrame, config: Dict) -> Dict:
    # Very simple checks: support if numeric thresholds exceeded
    if "low CTR" in hypo["statement"] or "low CTR" in hypo.get("expected_signals", []):
        # identify the campaign in statement (best effort)
        campaign_name = None
        if "Campaign" in hypo["statement"]:
            parts = hypo["statement"].split()
            try:
                campaign_name = parts[1]
            except:
                campaign_name = None
        if campaign_name:
            sub = df[df["campaign_name"].str.contains(campaign_name, na=False)]
        else:
            sub = df
        impressions = sub["impressions"].sum()
        clicks = sub["clicks"].sum()
        ctr = (clicks / impressions) if impressions else 0.0
        result = "supported" if ctr < 0.01 else "not_supported"
        evidence = {"ctr": ctr, "impressions": int(impressions), "clicks": int(clicks)}
        confidence = 0.7 if impressions > 100 else 0.4
        return {"hypothesis_id": hypo["hypothesis_id"], "result": result, "evidence": evidence, "confidence": confidence}
    # default
    return {"hypothesis_id": hypo["hypothesis_id"], "result": "inconclusive", "evidence": {}, "confidence": 0.3}
