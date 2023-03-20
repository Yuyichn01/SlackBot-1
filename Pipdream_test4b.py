import requests
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

text = []

def handler(pd: "pipedream"):
  count = 0
  global users
  TOKEN = f'{pd.inputs["slack_bot"]["$auth"]["bot_token"]}'
  authorization = f'Bearer {TOKEN}'
  headers = {"Authorization": authorization}
  r = requests.post('https://slack.com/api/auth.test', headers=headers)
  channel_id = pd.steps["w2"]["$return_value"][1]
  userID = str(pd.steps["w2"]["$return_value"][0])
  actionID = str(pd.steps["w2"]["$return_value"][3])
  number = int(actionID[6:])
  text = pd.steps["get_all_records"]["$return_value"]["text"]

    
  if text[number-1] == " ":
      text[number-1] = " is reserved by <@"+userID+">"
  else:
      text[number-1] = " "
      
  #slack API token
  client = WebClient(token=TOKEN)
  authorization = f'Bearer {TOKEN}'
  headers = {"Authorization": authorization}
  r = requests.get('https://slack.com/api/users.profile.get', headers=headers)

  result = client.chat_update(
        channel=channel_id, 
        blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Here is the :car: parking reservation form for today, please fill out by the end of the day*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :one:"+text[0]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action1",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :two:"+text[1]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action2",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :three:" + text[2]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action3",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :four:"+text[3]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action4",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :five:"+text[4]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action5",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :six:"+text[5]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action6",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :seven:" +text[6]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action7",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :eight:"+text[7]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action8",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :nine:"+text[8]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action9",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :keycap_ten:"+text[9]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action10",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :one::one:"+text[10]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action11",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :one::two:"+text[11]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action12",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :one::three:"+text[12]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action13",
				"style": "primary"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Badge Number :one::four:"+text[13]
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Reserve/Cancel"
				},
				"value": "click_me_123",
				"action_id": "action14",
				"style": "primary"
			}
        }
	],
        ts = pd.steps["w2"]["$return_value"][2]
    )
  return number,text
