from cgitb import text
from multiprocessing import Event
import os
import time
from typing import Text
import slack_sdk
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
import logging
from datetime import datetime
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.socket_mode import SocketModeHandler

#initialize bolt environment variables
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
channel1 = os.environ["channel_id1"]
conversation_history = []
logger = logging.getLogger(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'])

#listen to keyword "parking" and trigger events
@app.message("parking")
def message1(message, say):

    # welcome message
    say(f"Welcome to parking assistant <@{message['user']}>! ")
    say(f"Please enter your desired parking number (1 to 14): ")

@app.event("app_mention",)
def event1(say):
    say("Hi there!")
    say("what can i help you? ")
    
        
    

# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
 
