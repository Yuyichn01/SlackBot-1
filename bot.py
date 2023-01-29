import os
from pathlib import Path
import datetime
import time
import logging
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.socket_mode import SocketModeHandler

# parking information class
class staffParkingInfo:
    def __init__(self, name, parkingNumber):
     self.name = name
     self.parkingNumber = parkingNumber

#create a array of staffParkingInfo class
parkingInfoArrayToday = []
parkingInfoArrayTomorrow = []
parkingInfoArrayEmpty = []
indexArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in indexArray:
    parkingInfoArrayToday.append(staffParkingInfo("empty",i))
    parkingInfoArrayTomorrow.append(staffParkingInfo("empty",i))
    parkingInfoArrayEmpty.append(staffParkingInfo("empty",i))

#initialize bolt environment variables
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
channel1 = os.environ["channel_id1"]
logger = logging.getLogger(__name__)

#when the user @the robot
@app.event("app_mention")
def event1(event,say):
      user_id = event["user"]
      text = event["text"]
      say(f"Hello <@{user_id}>! I am slack bot")
      say(f"for parking please enter 'reserve parking'+'your name ")

@app.message("^help$")
def message1(message,say):
    text = message["text"]
    say(f"Hello! What can I help you?")

#reserve parking method
@app.message("reserve parking")
def message1(message,say):
    num = 0
    text = message["text"]
    noAvailableSpots = True
    for i in parkingInfoArrayTomorrow:
      if i.name == "empty":
        num = str(i.parkingNumber)
        i.name = text[16:]
        noAvailableSpots = False
        break
    if noAvailableSpots == True:
        say(f"Sorry, no parking spot available")
    else:
        say(f"you have successfully reserved badge number "+ num + ", please collect your badge at IT room")

#print parking information method   
@app.message("^parking info$")   
def outputParkingInfo(say):
    text = "Number:         Status:\n"
    for j in parkingInfoArrayToday:
        if j.name == "empty":
          text += str(j.parkingNumber)+"                      available\n"
        else:
            if j.name =="":
                text +=str(j.parkingNumber) + "                     reserved, name not entered\n"
            else:
                text +=str(j.parkingNumber) + "                     reserved by "+ j.name + "\n"
    say(text)
        
# Start app
if __name__ == "__main__":
    #if the scheduled time is reached, switch today's info to tomorrow and restore tomorrow's info
    if (datetime.datetime.now()==datetime.time(hour=23, minute=30)):
       parkingInfoArrayToday = parkingInfoArrayTomorrow
       parkingInfoArrayTomorrow = parkingInfoArrayEmpty
    if (datetime.datetime.now()==datetime.time(hour=12, minute=00)):
          result = client.chat_postMessage(
          channel=channel1,
          thread_ts=time.time(),
          text="The parking reservation ended, enter 'parking info' to check your parking number!")
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

