import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import pandas as pd
import json


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

    metadata = body["channel"]["id"] + "-" + body["message_ts"] + "-" + body["message"]["thread_ts"]
    solution = body["message"]["text"]

    result = client.conversations_history(
        channel=body["channel"]["id"],
        inclusive=True,
        oldest=body["message"]["thread_ts"],
        limit=1
    )

    problem = result["messages"][0]["text"]    
    
    # Call the views_open method using the built-in WebClient
    result = client.views_open(
        trigger_id=shortcut["trigger_id"],
        
        # A simple view payload for a modal
        view = {
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "New Knowladge Base Entry",
                "emoji": True
            },
            "private_metadata": metadata,
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "block_id": "product",
                    "type": "input",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a Product",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Nexus IQ CLI",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Nexus IQ Jenkins Plugin",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Nexus IQ Jira Plugin",
                                    "emoji": True
                                },
                                "value": "value-2"
                            }
                        ],
                        "action_id": "static_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Integrations Product",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "block_id": "problem",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action",
                        "initial_value": problem
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Problem / Question",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "block_id": "solution",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action",
                        "initial_value": solution
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Solution / Response",
                        "emoji": True
                    }
                }
            ]
        }
    )

@app.view("")
def handle_view_events(ack, client, body):
    ack()
    
    metadata = body["view"]["private_metadata"].split("-")
    selected_product = body["view"]["state"]["values"]["product"]["static_select-action"]["selected_option"]["value"]
    problem_question = body["view"]["state"]["values"]["problem"]["plain_text_input-action"]["value"]
    solution_response = body["view"]["state"]["values"]["solution"]["plain_text_input-action"]["value"]
    channel = metadata[0]
    message_ts = metadata[1]
    thread_ts = metadata[2]
    
    response = client.chat_getPermalink(
        channel=channel,
        message_ts=message_ts
    )
    message_link = response.data["permalink"]

    response = client.chat_getPermalink(
        channel=channel,
        message_ts=thread_ts
    )
    thread_link = response.data["permalink"]

    entry = [{
        "Channel": channel,
        "Message Id": message_ts,
        "Thread Id": thread_ts,
        "Product": selected_product,
        "Problem/Question": problem_question,
        "Solution/Response": solution_response,
        "Message Link": message_link,
        "Thread Link": thread_link
    }]
    
    print('Result: ', entry)

    df = pd.read_csv('data.csv', sep='|')
    row = pd.DataFrame(entry)
    df = pd.concat([df, row])
    df.to_csv('data.csv', encoding='utf-8', sep='|', index=False)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()