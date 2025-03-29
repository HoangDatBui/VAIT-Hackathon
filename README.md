# Server Engagement Bot (SEB)

## Quick Start:

1. Clone this repo and `cd` into it
2. Create new Python virtual environment: `python3 -m venv bot-env`
3. Activate the virtual environment: `source bot-env/bin/activate`
4. Install required packages: `pip install -r requirements.txt`
5. Add `DISCORD_TOKEN`, `DEEPSEEK_API_KEY` environment variables
6. Start the bot: `python main.py`

## Note when adding new packages:

After adding new packages using `pip install`, make sure to update `requirements.txt` using
`pip freeze > requirements.txt`. This locks down the versions of all installed packages
and prevents future package management issues.
