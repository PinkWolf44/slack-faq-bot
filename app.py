import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/integrations-bot")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(event, say):
    say(f"Hi there, <@{event['user']}>!")

@app.shortcut("open_modal")
def open_modal(ack, shortcut, client, body):
    # Acknowledge the shortcut request
    ack()
    print('Body: ',body)
    # Call the views_open method using the built-in WebClient
    client.views_open(
        trigger_id=shortcut["trigger_id"],
        # A simple view payload for a modal
        view={
            "type": "modal",
            "title": {"type": "plain_text", "text": "My App"},
            "close": {"type": "plain_text", "text": "Close"},
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "About the simplest modal you could conceive of :smile:\n\nMaybe <https://api.slack.com/reference/block-kit/interactive-components|*make the modal interactive*> or <https://api.slack.com/surfaces/modals/using#modifying|*learn more advanced modal use cases*>."
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Psssst this modal was designed using <https://api.slack.com/tools/block-kit-builder|*Block Kit Builder*>"
                        }
                    ]
                }
            ]
        }
    )

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()