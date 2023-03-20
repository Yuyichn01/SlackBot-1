import requests
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError



def handler(pd: "pipedream"):
  TOKEN = f'{pd.inputs["slack_bot"]["$auth"]["bot_token"]}'
  authorization = f'Bearer {TOKEN}'
  headers = {"Authorization": authorization}
  r = requests.post('https://slack.com/api/auth.test', headers=headers)
  channel_id = pd.steps["trigger"]["event"]["body"]["channel_id"]
  
  #slack API token
  client = WebClient(token=TOKEN)
  authorization = f'Bearer {TOKEN}'
  headers = {"Authorization": authorization}
  r = requests.get('https://slack.com/api/users.profile.get', headers=headers)

  result = client.chat_postMessage(
        channel=channel_id, 
        blocks =[
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
				"text": "Badge Number :one:"
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
				"text": "Badge Number :two:"
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
				"text": "Badge Number :three:"
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
				"text": "Badge Number :four:"
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
				"text": "Badge Number :five:"
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
				"text": "Badge Number :six:"
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
				"text": "Badge Number :seven:"
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
				"text": "Badge Number :eight:"
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
				"text": "Badge Number :nine:"
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
				"text": "Badge Number :keycap_ten:"
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
				"text": "Badge Number :one::one:"
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
				"text": "Badge Number :one::two:"
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
				"text": "Badge Number :one::three:"
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
				"text": "Badge Number :one::four:"
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
	]
    )
