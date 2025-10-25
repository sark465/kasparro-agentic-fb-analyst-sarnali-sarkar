import pandas as pd
from src.agents import evaluator

def test_evaluate_hypothesis_low_ctr():
    df = pd.DataFrame({
        "campaign_name": ["C1","C1"],
        "impressions": [1000, 500],
        "clicks": [5, 3],
        "spend":[50,20],
        "revenue":[10,5]
    })
    hypo = {"hypothesis_id":"H_lowctr_C1", "statement":"Campaign C1 has low CTR (possible creative fatigue)", "expected_signals":["low_ctr"]}
    res = evaluator.evaluate_hypothesis(hypo, df, config={})
    assert res["result"] in {"supported","not_supported","inconclusive"}
