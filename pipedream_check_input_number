import requests
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

indexArray = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
isCorrect = False

def handler(pd: "pipedream"):
  # variables declared for use in next workflow
  global count
  global isCorrect
  global timeStamp
  user = pd.steps["trigger"]["event"]["user"]
  timeStamp = pd.steps["trigger"]["event"]["thread_ts"]
  text = pd.steps["trigger"]["event"]["text"]
  
  #slack API token
  TOKEN = pd.inputs["slack"]["$auth"]["oauth_access_token"]
  authorization = f'Bearer {TOKEN}'
  headers = {"Authorization": authorization}
  r = requests.get('https://slack.com/api/users.profile.get', headers=headers)
  
  for i in indexArray:
       if text == i:
         isCorrect = True
         break
  
  return text,isCorrect,user,timeStamp
