## USER SETTINGS

# INPUT THE 2 SLACK TEAM NAMES YOU WISH TO LINK BELOW
#   Slack team names are the first part of the slack web address
#   i.e. team-name.slack.com
#
slack1 = ""
slack2 = ""

# INPUT THE 2 SLACK INCOMING WEBHOOKS BELOW
#   Slack webhooks are typically in the format https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYYY/ZZZZZZZZZZZZZZZZZZZZZZZZ
#
slack1_incoming = ""
slack2_incoming = ""

## WARNING: MODIFYING THE CODE BELOW MAY BREAK THINGS

# Avoids creating a Slackbot echo loop
if input_data['username'] == "slackbot":
    return

import json

message = { 'icon_emoji': ':slack:', 'text': input_data['text'], 'username': input_data['username'] + "@" + input_data['team_domain'] }

if input_data['team_domain'] == slack1:
    webhook_url = slack2_incoming

if input_data['team_domain'] == slack2:
    webhook_url = slack1_incoming

response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
