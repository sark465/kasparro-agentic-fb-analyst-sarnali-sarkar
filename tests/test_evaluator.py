# tests/test_evaluator.py
import unittest
import pandas as pd
from src.agents import evaluator

class TestEvaluator(unittest.TestCase):

    def test_evaluate_hypothesis_low_ctr(self):
        df = pd.DataFrame({
            "campaign_name": ["C1","C1"],
            "impressions": [1000, 500],
            "clicks": [5, 3],
            "spend":[50,20],
            "revenue":[10,5]
        })
        hypo = {
            "hypothesis_id":"H_lowctr_C1",
            "statement":"Campaign C1 has low CTR (possible creative fatigue)",
            "expected_signals":["low_ctr"]
        }
        res = evaluator.evaluate_hypothesis(hypo, df, config={})

        # Print and save result for visibility
        print("Evaluator output:", res)
        with open("test_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Evaluator output: {res}\n")
        
        # Actual test assertion
        self.assertIn(res["result"], {"supported","not_supported","inconclusive"})

if __name__ == "__main__":
    unittest.main()
