from typing import List, Dict

def generate_creatives_for_campaign(campaign_name: str, sample_messages: List[str]) -> Dict:
    # produce 3 variants grounded in sample messages
    variants = []
    base = sample_messages[:3] if sample_messages else ["Comfortable fit", "Soft fabric", "All-day wear"]
    calls_to_action = ["Shop now", "Grab yours", "Limited stock"]
    for i, b in enumerate(base):
        variants.append({
            "headline": f"{b} — Feel the comfort",
            "body": f"{b}. Try our new undergarments designed for all-day comfort. {b}",
            "cta": calls_to_action[i % len(calls_to_action)],
            "rationale": f"Remix of existing message: '{b}' to emphasize benefit and add CTA."
        })
    return {"campaign_name": campaign_name, "creative_recommendations": variants}

def generate_creatives(low_ctr_campaigns: List[Dict]) -> List[Dict]:
    out = []
    for c in low_ctr_campaigns:
        sample_msgs = c.get("sample_messages", [])
        out.append(generate_creatives_for_campaign(c.get("campaign_name","unknown"), sample_msgs))
    return out
