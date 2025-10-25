Planner Agent
--------------
Input: user_query (string), data_summary (dict)

Output format (JSON):
{
  "tasks": [
    {"name":"load_data","args":{}},
    {"name":"summarize_data","args":{}},
    {"name":"generate_hypotheses","args":{}},
    {"name":"validate_hypotheses","args":{}},
    {"name":"generate_creatives","args":{}}
  ]
}

Reasoning: Think -> Decompose -> Output a structured plan with short justification for each task.
