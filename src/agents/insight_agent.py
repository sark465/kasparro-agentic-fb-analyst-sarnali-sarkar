from typing import List, Dict
import numpy as np

def generate_hypotheses(data_summary: Dict) -> List[Dict]:
    # example heuristics
    hypos = []
    if data_summary["overall_roas"] and data_summary["overall_roas"] < 1.0:
        hypos.append({
            "hypothesis_id":"H1",
            "statement":"Overall ROAS is below 1.0 indicating unprofitable campaigns",
            "rationale":"Aggregate revenue < spend",
            "expected_signals":["roas < 1", "low purchases"],
            "confidence":0.6
        })
    # Hypothesis example for low CTR campaigns
    for c in data_summary.get("by_campaign", [])[:3]:
        ctr = (c.get("clicks",0) / c.get("impressions",1)) if c.get("impressions",0) else 0
        if ctr < 0.01:
            hypos.append({
                "hypothesis_id": f"H_lowctr_{c['campaign_name']}",
                "statement": f"Campaign {c['campaign_name']} has low CTR (possible creative fatigue)",
                "rationale": f"Observed CTR ~ {ctr:.4f}",
                "expected_signals":["low_ctr","high_impressions","low_clicks"],
                "confidence":0.5
            })
    return hypos
