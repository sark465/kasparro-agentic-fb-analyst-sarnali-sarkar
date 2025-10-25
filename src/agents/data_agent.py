import pandas as pd
from typing import Dict
from pathlib import Path
import yaml

def load_config(path="config/config.yaml"):
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)

def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["date"])
    return df

def summarize_data(df: pd.DataFrame) -> Dict:
    total_spend = float(df["spend"].sum())
    total_revenue = float(df["revenue"].sum())
    overall_roas = total_revenue / total_spend if total_spend else None
    # Basic aggregates by campaign
    by_campaign = (
        df.groupby("campaign_name")
        .agg(spend=("spend", "sum"), revenue=("revenue", "sum"),
             impressions=("impressions", "sum"), clicks=("clicks", "sum"))
        .reset_index()
        .to_dict(orient="records")
    )
    return {
        "n_rows": len(df),
        "total_spend": total_spend,
        "total_revenue": total_revenue,
        "overall_roas": overall_roas,
        "by_campaign": by_campaign,
    }
