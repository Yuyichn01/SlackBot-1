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

import os, time, datetime, json, logging
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient
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

# Open and update JSON file
def updateData():
 with open("data.json") as f:
    data = json.load(f)
    for i in indexArray:
      data[str(i)] = parkingInfoArrayTomorrow[i-1].name
      json.dump(data, open("data.json", "w"), indent = 4)
    
#when the user @the robot
@app.event("app_mention")
def event1(event,say):
    user_id = event["user"]
    text = event["text"]
    say(f"Hello <@{user_id}>, I am slack bot! What can I help you with?\n"
        f"-please type 'parking info today' to check today's parking information\n"
        f"-please type 'parking info' to check tomorrow's parking information\n"
        f"-please type 'reserve parking' to book a parking badge\n")

@app.message("^help$")
def message1(message,say):
    user_id = message["user"]
    text = message["text"]
    say(f"Hello <@{user_id}>, I am slack bot! What can I help you with?\n"
        f"-please type 'parking info today' to check today's parking information\n"
        f"-please type 'parking info' to check tomorrow's parking information\n"
        f"-please type 'reserve parking' to book a parking badge\n")
    
#reserve parking
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
    updateData()

#print parking information for today
@app.message("^parking info today$")   
def outputParkingInfo(say):
    text = f"parking info today:\n"
    text += "Number:         Status:\n"
    for j in parkingInfoArrayToday:
        if j.name == "empty":
          text += str(j.parkingNumber)+"                      available\n"
        else:
            if j.name ==" ":
                text +=str(j.parkingNumber) + "                     reserved, name not entered\n"
            else:
                text +=str(j.parkingNumber) + "                     reserved by "+ j.name + "\n"
    say(text)
    
#print parking information for today
@app.message("^parking info tomorrow$")   
def outputParkingInfo(say):
    text = f"parking info tomorrow:\n"
    text += "Number:         Status:\n"
    for j in parkingInfoArrayTomorrow:
        if j.name == "empty":
          text += str(j.parkingNumber)+"                      available\n"
        else:
            if j.name ==" ":
                text +=str(j.parkingNumber) + "                     reserved, name not entered\n"
            else:
                text +=str(j.parkingNumber) + "                     reserved by "+ j.name + "\n"
    say(text)

# Start app
if __name__ == "__main__":
    #siwtch data if the scheduled time is reached
    if (datetime.datetime.now()==datetime.time(hour=23, minute=30)):
       parkingInfoArrayToday = parkingInfoArrayTomorrow
       parkingInfoArrayTomorrow = parkingInfoArrayEmpty
    if (datetime.datetime.now()==datetime.time(hour=12, minute=00)):
          result = client.chat_postMessage(channel=channel1,thread_ts=time.time(),text="The parking reservation ended, enter 'parking info' to check your parking number!")
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
