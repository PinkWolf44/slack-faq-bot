
import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ──────────────────────────────────
load_dotenv()
app = App(token=os.environ["SLACK_BOT_TOKEN"])
PERSONA = """
You are Jeff Bezos, founder of Amazon.
• Relentlessly customer-obsessed, data-driven, long-term-oriented.
• Speak in short, direct sentences, ask probing questions.
• Use phrases like “Day 1”, “disagree and commit”.
• When unsure, say: “I need more data before deciding.” 🤖
• End every answer with the 🤖 emoji.
"""

from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.event("app_mention")
def handle_mention(event, say):
    user_text = event.get("text", "")
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": PERSONA},
                {"role": "user",   "content": user_text},
            ],
            temperature=0.7,
        )
        reply = completion.choices[0].message.content
    except Exception as e:
        reply = f"OpenAI error: {e} 🤖"
    say(reply)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
