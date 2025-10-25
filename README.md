# kasparro-agentic-fb-analyst-sarnali-sarkar
Multi-agent AI system for diagnosing Facebook Ads performance and generating creative recommendations.
# kasparro-agentic-fb-analyst-sarnali-sarkar

## Quick start (Windows)

```powershell
# clone (if not already)
git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst-sarnali-sarkar.git
cd kasparro-agentic-fb-analyst-sarnali-sarkar

# create venv
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# ensure dataset path in config/config.yaml is correct
python src/run.py "Analyze ROAS drop in last 7 days"
