# Slack Zapier Bridge
Creates a bridged (shared) channel between two Slack teams with this code snippet and zapier.com!

## Prerequisites
 - An account on zapier.com (free tier will work fine)
 - The power to create webhooks on 2 Slack teams

## Instructions
1. Create a new Zap on Zapier.
2. Zap Trigger = Catch Hook
3. (Leave Child Key blank)
4. Copy the generated webhook URL and save it somewhere.
5. (Don't continue to the Action setup yet, but keep the zapier browser tab open)
6. In a different browser tab, open up the Slack Custom Integrations settings.
  - These should be at https://your-team-name.slack.com/apps/manage/custom-integrations
7. Create an Outgoing Webhook
8. Select a channel for the Outgoing Webhook. This will be the shared channel between the 2 Slack teams.
9. In URLs, paste the generated Zapier webhook URL from step 4.
10. (it may also be a good idea to customize the name of the webhook to something like "slack-bridge")
11. Save the settings.
12. Go to the channel you selected in step 8 and type a test message. _Required for the next step!_
13. Go back to the Zapier tab and click the OK button.
14. (You should get a Test Successful message) Click Continue.
14. Zap Action = Python Code
15. Configure the Run Python Input Data:
  1. Left box = "text". Right box, select the Catch Hook "Text" field from the dropdown.
  2. Left box = "username". Right box, select the Catch Hook "User Name" field from the dropdown.
  3. Left box = "team_domain". Right box, select the Catch Hook "Team Domain" field from the dropdown.
16. Paste the code from slack-bridge-zap.py in the Code box.
17. [TO BE CONTINUED]
