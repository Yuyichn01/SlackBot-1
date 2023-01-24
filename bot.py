from ast import Num
from cgitb import text
from email import message
from multiprocessing import Event
import os
import time
from typing import Text
from pathlib import Path
from xml.etree.ElementTree import tostring
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

#variables to declare
input = ["^number 1$",
        "^number 2$",
        "^number 3$",
        "^number 4$",
        "^number 5$",
        "^number 6$",
        "^number 7$",
        "^number 8$",
        "^number 9$",
        "^number 10$",
        "^number 11$",
        "^number 12$",
        "^number 13$",
        "^number 14$"]

parkingInfoArray = [0]*14

#initialize bolt environment variables
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
channel1 = os.environ["channel_id1"]
 
#when the user @the robot
@app.event("app_mention")
def event1(event,say):
      user_id = event["user"]
      text = event["text"]
      say(f"Hello <@{user_id}>! I am slack bot")
      say(f"for parking please enter 'parking reservation' ")

#listen to keyword "parking" and trigger events
@app.message("^parking reservation$")
def message1(say):
    # welcome message
    say(f"Please enter 'number'+ 'your desired parking number (1 to 14)', Eg:number 14, number 01")
    
#listen to keyword "parking" and trigger events
for i in input:
  @app.message(i)
  def message1(message, say):
    text = message["text"]
    reserved = False
    if parkingInfoArray[int(text[7:9])-1]!= 0:
        say("number " + text[7:9]+ " is reserved, please try a different parking number")
    else:
        parkingInfoArray[int(text[7:9])-1]= int(text[7:9])
        say(text +" has been reserved successfully!")

#print parking information method   
@app.message("^parking information$")   
def outputParkingInfo(say):
    num=0
    for i in input:
        if parkingInfoArray[num] == 0:
          say(input[num]+" is available")
        else:
          say(input[num]+" is reserved")
        num +=1

# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
 
 
