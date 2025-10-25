import argparse
import yaml
import pandas as pd
from src.agents import planner, data_agent, insight_agent, evaluator as ev, creative_generator
from src.utils.io_utils import save_json, ensure_dir
import os
from datetime import datetime
import json

LOG_PATH = "logs/run_log.json"
CONFIG_PATH = "config/config.yaml"

def main(query):
    cfg = data_agent.load_config(CONFIG_PATH)
    csv_path = cfg["DATA_CSV"]
    df = data_agent.load_data(csv_path)
    data_summary = data_agent.summarize_data(df)

    # Planner
    plan = planner.plan_from_query(query)

    # Insight generation
    hypos = insight_agent.generate_hypotheses(data_summary)

    # Evaluation
    evaluations = []
    for h in hypos:
        res = ev.evaluate_hypothesis(h, df, cfg)
        # attach statement for readability
        res["statement"] = h["statement"]
        evaluations.append(res)

    # Identify low CTR campaigns to feed creative generator
    # Simple heuristic: overall campaign CTR < 1%
    low_ctr_campaigns = []
    for c in data_summary.get("by_campaign", []):
        impressions = c.get("impressions", 0)
        clicks = c.get("clicks", 0)
        ctr = (clicks / impressions) if impressions else 0
        if ctr < 0.01:
            low_ctr_campaigns.append({"campaign_name": c["campaign_name"], "sample_messages": ["Comfortable fit", "Try now"]})

    creatives = creative_generator.generate_creatives(low_ctr_campaigns)

    # Persist outputs
    output_dir = cfg.get("output_dir", "reports")
    ensure_dir(output_dir)
    save_json({"hypotheses": hypos}, os.path.join(output_dir, "insights.json"))
    save_json({"evaluations": evaluations}, os.path.join(output_dir, "evaluations.json"))
    save_json({"creatives": creatives}, os.path.join(output_dir, "creatives.json"))

    # Minimal human-readable report
    with open(os.path.join(output_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write("# Kasparro Agentic FB Analyst Report\n\n")
        f.write(f"Query: {query}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- total rows: {data_summary['n_rows']}\n")
        f.write(f"- total spend: {data_summary['total_spend']}\n")
        f.write(f"- overall ROAS: {data_summary['overall_roas']}\n\n")
        f.write("## Top Hypotheses\n")
        for h in hypos:
            f.write(f"- {h['hypothesis_id']}: {h['statement']} (confidence: {h['confidence']})\n")
    print(f"Outputs written to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Analysis query (e.g., 'Analyze ROAS drop in last 7 days')")
    args = parser.parse_args()
    main(args.query)
