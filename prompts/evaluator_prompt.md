Evaluator Agent
---------------
Input: hypothesis, raw_data_summary

Output JSON:
{
 "hypothesis_id":"H1",
 "result":"supported"/"not_supported"/"inconclusive",
 "metric_checks":[
   {"metric":"ctr","baseline":0.03,"current":0.015,"p_value":0.01}
 ],
 "confidence":0.7,
 "evidence":"short textual explanation"
}

Guidance: use simple statistical checks and thresholds from config. If sample size small, return inconclusive.
