# slack-faq-bot
Slack bot that helps to create a Questions &amp; Answers database and helps to automatically answer to 
frequently asked questions

## How to run

### Prepare the environment
Before running the app you need to follow the next steps to prepare the environment:

```bash
# For Linux
python3 -m venv .venv
source .venv/bin/activate
export SLACK_BOT_TOKEN=xapp-<your-app-token>
export SLACK_APP_TOKEN=xoxb-<your-bot-token>
pip install slack_bolt

# For Windows
py -m venv env
.\env\Scripts\activate
set SLACK_BOT_TOKEN=xapp-<your-app-token>
set SLACK_APP_TOKEN=xoxb-<your-bot-token>
pip install slack_bolt
```

### Run the app
You will need to execute the next command:
```bash
# For Linux
python3 app.py

# For Windows
py app.py
```

## Docs
Slack docs: https://api.slack.com/docs
Bolt SDKs: https://api.slack.com/tools/bolt
Bolt Python SDK: https://slack.dev/bolt-python/concepts
