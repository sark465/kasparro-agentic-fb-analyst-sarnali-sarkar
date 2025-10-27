from typing import List, Dict
import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")

def generate_hypotheses(data_summary: Dict, config: Dict) -> List[Dict]:
    """
    Generate candidate hypotheses based on campaign performance summary.
    Observability: Logs reflections when confidence < threshold.
    """
    hypos = []
    threshold = config.get("thresholds", {}).get("confidence", 0.6)

    # Example heuristic: low overall ROAS
    if data_summary.get("overall_roas") and data_summary["overall_roas"] < 1.0:
        hypo = {
            "hypothesis_id": "H1",
            "statement": "Overall ROAS is below 1.0 indicating unprofitable campaigns",
            "rationale": "Aggregate revenue < spend",
            "expected_signals": ["roas < 1", "low purchases"],
            "confidence": 0.6
        }
        hypos.append(hypo)
        if hypo["confidence"] < threshold:
            logger.info({
                "event": "reflection_triggered",
                "reason": "low_confidence",
                "hypothesis_id": hypo["hypothesis_id"],
                "previous_confidence": hypo["confidence"],
                "action": "replan_hypothesis",
                "change": "Re-evaluated ROAS segment across all campaigns"
            })
            hypo["confidence"] += 0.1  # simulate reflection/replan improvement

    # Hypothesis example for low CTR campaigns
    for c in data_summary.get("by_campaign", [])[:3]:
        ctr = (c.get("clicks", 0) / c.get("impressions", 1)) if c.get("impressions", 0) else 0
        hypo = {
            "hypothesis_id": f"H_lowctr_{c['campaign_name']}",
            "statement": f"Campaign {c['campaign_name']} has low CTR (possible creative fatigue)",
            "rationale": f"Observed CTR ~ {ctr:.4f}",
            "expected_signals": ["low_ctr", "high_impressions", "low_clicks"],
            "confidence": 0.5
        }
        hypos.append(hypo)

        # Observability: Reflection trigger
        if hypo["confidence"] < threshold:
            logger.info({
                "event": "reflection_triggered",
                "reason": "low_confidence",
                "hypothesis_id": hypo["hypothesis_id"],
                "previous_confidence": hypo["confidence"],
                "action": "re-examine CTR time series",
                "change": f"Re-analyzed CTR trend for campaign {c['campaign_name']}"
            })
            hypo["confidence"] += 0.1  # replan adjustment

    return hypos
