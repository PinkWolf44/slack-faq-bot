import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import entry_view_builder
import entry_storage_service
from entry_view_service import EntryViewService
from entry_service import EntryService


# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/integrations-bot")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(event, say):
    say(f"Hi there, <@{event['user']}>!")

@app.shortcut("open_entry_view")
def open_modal(ack, shortcut, client, body):
    # Acknowledge the shortcut request
    ack()

    # Get the new entry form data    
    data = EntryViewService(body, client).get_entry_view_data()

    # Building the modal view
    new_entry_view = entry_view_builder.build_view(data)
    
    # Call the views_open method using the built-in WebClient
    result = client.views_open(
        trigger_id=shortcut['trigger_id'],
        view = new_entry_view
    )

@app.view("")
def handle_view_events(ack, client, body):
    ack()
    
    # Get new entry record data
    data = EntryService(body, client).get_entry_data()

    # Store the new record
    entry_storage_service.store_entry(data)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
