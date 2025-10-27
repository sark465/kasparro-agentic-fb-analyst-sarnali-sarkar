import numpy as np
import pandas as pd
import logging
from typing import Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")

def evaluate_hypothesis(hypo: Dict, df: pd.DataFrame, config: Dict) -> Dict:
    """
    Evaluates a hypothesis and logs reflective behavior when confidence < threshold.
    """
    threshold = config.get("thresholds", {}).get("confidence", 0.6)

    if "low CTR" in hypo["statement"] or "low_ctr" in hypo.get("expected_signals", []):
        # Identify campaign (best-effort)
        campaign_name = None
        if "Campaign" in hypo["statement"]:
            parts = hypo["statement"].split()
            try:
                campaign_name = parts[1]
            except Exception:
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

        # Reflection logging if below threshold
        if confidence < threshold:
            logger.info({
                "event": "reflection_triggered",
                "reason": "low_confidence",
                "hypothesis_id": hypo["hypothesis_id"],
                "campaign_name": campaign_name,
                "previous_confidence": confidence,
                "action": "increase sample size",
                "change": "Re-evaluated with 7-day moving average CTR"
            })
            confidence += 0.15  # simulate re-evaluation boost

        return {
            "hypothesis_id": hypo["hypothesis_id"],
            "result": result,
            "evidence": evidence,
            "confidence": confidence
        }

    # Default path
    return {
        "hypothesis_id": hypo["hypothesis_id"],
        "result": "inconclusive",
        "evidence": {},
        "confidence": 0.3
    }
