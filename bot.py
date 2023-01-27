import os
from pathlib import Path
from pickle import NONE
from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

# parking information class
class staffParkingInfo:
    name="empty"
    parkingNumber = 0

#create a array of staffParkingInfo class
p1 = staffParkingInfo() 
p2 = staffParkingInfo() 
p3 = staffParkingInfo() 
p4 = staffParkingInfo() 
p5 = staffParkingInfo() 
p6 = staffParkingInfo() 
p7 = staffParkingInfo() 
p8 = staffParkingInfo() 
p9 = staffParkingInfo() 
p10 = staffParkingInfo() 
p11 = staffParkingInfo() 
p12 = staffParkingInfo() 
p13 = staffParkingInfo() 
p14 = staffParkingInfo() 
parkingInfoArray = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]

p1.parkingNumber = 1
p2.parkingNumber = 2
p3.parkingNumber = 3
p4.parkingNumber = 4
p5.parkingNumber = 5
p6.parkingNumber = 6
p7.parkingNumber = 7
p8.parkingNumber = 8
p9.parkingNumber = 9
p10.parkingNumber = 10
p11.parkingNumber = 11
p12.parkingNumber = 12
p13.parkingNumber = 13
p14.parkingNumber = 14

for i in parkingInfoArray:
    print(i.parkingNumber)

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
    for i in parkingInfoArray:
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
@app.message("^parking information$")   
def outputParkingInfo(say):
    text = "Number:         Status:\n"
    for j in parkingInfoArray:
        if j.name == "empty":
          text += str(j.parkingNumber)+"                      available\n"
        else:
            if j.name =="":
                text +=str(j.parkingNumber) + "                     reserved\n"
            else:
                text +=str(j.parkingNumber) + "                     reserved by "+ j.name + "\n"
    say(text)
        
# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

