# kasparro-agentic-fb-analyst-sarnali-sarkar
Multi-agent AI system for diagnosing Facebook Ads performance and generating creative recommendations.

# Project structure (create these files & folders)

kasparro-agentic-fb-analyst-sarnali-sarkar/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ config/
│ └─ config.yaml
├─ data/
│ └─ synthetic_fb_ads_undergarments.csv # Local dataset path
├─ prompts/
│ ├─ planner_prompt.md
│ ├─ insight_prompt.md
│ ├─ evaluator_prompt.md
│ └─ creative_prompt.md
├─ src/
│ ├─ run.py
│ ├─ agents/
│ │ ├─ planner.py
│ │ ├─ data_agent.py
│ │ ├─ insight_agent.py
│ │ ├─ evaluator.py
│ │ └─ creative_generator.py
│ └─ utils/
│ └─ io_utils.py
├─ reports/
│ ├─ report.md
│ ├─ insights.json
│ └─ creatives.json
├─ tests/
│ └─ test_evaluator.py
└─ Makefile (optional)

## Quick Start (Windows)

1. **Clone the repository**  
   ```powershell
   git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst-sarnali-sarkar.git
   cd kasparro-agentic-fb-analyst-sarnali-sarkar

2.  **Check Python version (>= 3.10):**

python -V


3. **Create and activate a virtual environment:**

python -m venv env1
.\env1\Scripts\activate


4. **Upgrade pip and essential tools:**

python -m pip install --upgrade pip setuptools wheel


5. **Install project dependencies:**

pip install -r requirements.txt


6. **Run the main analysis:**

python src/run.py "Analyze ROAS drop in last 7 days"

7. **Data**

Place the full CSV locally and set the environment variable:

set DATA_CSV=D:\VS_CODE_PROJECTS\kasparro-agentic-fb-analyst-sarnali-sarkar\synthetic_fb_ads_undergarments.csv


Or copy a small sample to data/sample_fb_ads.csv.

See data/README.md for more details.

8. **Configuration**

Edit config/config.yaml to customize parameters:

python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: true

9. **Repository Structure**

src/agents/ — planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py

prompts/ — Markdown prompt templates with variable placeholders

reports/ — report.md, insights.json, creatives.json

logs/ — JSON traces for observability

tests/ — test_evaluator.py

10. **Running Tests**
python -m unittest discover -s tests

11. **Outputs**

reports/report.md — Summary report for marketers

reports/insights.json — Structured insights & hypotheses

reports/creatives.json — Recommended creative messages

12. **Observability**

Save Langfuse screenshots or JSON logs in reports/observability/ to track model performance.

13. **Release**

Tag release as v1.0 in GitHub and the release link is : https://github.com/sark465/kasparro-agentic-fb-analyst-sarnali-sarkar/releases/tag/v1.0


14. **Self-Review**

Include a PR describing design decisions, tradeoffs, and reasoning for full transparency.

✅ This version is **fully beginner-friendly**, with a one-liner setup command for Windows that:  
- Creates & activates the environment  
- Upgrades pip and tools  
- Installs dependencies  
- Runs the main analysis  


