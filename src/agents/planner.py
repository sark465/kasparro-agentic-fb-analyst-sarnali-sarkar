from typing import List, Dict

def plan_from_query(user_query: str) -> Dict:
    # simple rule-based planner mapping to tasks
    tasks = [
        {"name": "load_data", "args": {}},
        {"name": "summarize_data", "args": {}},
        {"name": "generate_hypotheses", "args": {"focus": user_query}},
        {"name": "validate_hypotheses", "args": {}},
        {"name": "generate_creatives", "args": {"focus": "low_ctr"}},
    ]
    return {"query": user_query, "tasks": tasks}
