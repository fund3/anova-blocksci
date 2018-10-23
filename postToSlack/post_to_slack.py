"""
    post_to_slack.py

When this script is run, it will check the difference in crypto wallet balances between two
# dates and if the difference in balance is significant, it will send a notification to the
# FUND3 slack channel
"""

import datetime
import sys
import json
import blocksci
import numpy as np
import pandas as pd

# sys.path.append("..")
sys.path.append("../../")

from slackclient import SlackClient
from services.transactions import get_top_transactions




class failedPost(Exception):
    pass

"""
Simple Util class to send a slack message notification.
"""
class SlackUtil:
    """
    Official Slack API Reference: https://github.com/slackapi/python-slackclient
    Simple Util class to send a slack message notification.
    For now, the functionality is rather simple - just sending a message.
    But in the future logging should be incorporated and this could be developed
    into a full slackbot wrapper.
    TODOs:
    1. Figure out how to search and store all slack channel/ user IDs and
    keep a list instead of using #channelname
    """
    def __init__(self, auth_token):
        """
        Need a better way to store auth_tokens aside from env vars.
        :param auth_token:
        """
        self.client = SlackClient(auth_token)

    def send_message(self, channel, message, botname):
        """
        Sends a message to a channel with botname.
        TODO (calvinleungyk): Extend to adding icon/ emoji url for the bot.
        Example usage:
            slack_util = SlackUtil(auth_token)
            slack_util.send_message('random', 'This is a test message.',
                                    'botname')
        :param channel: str, name of the channel to send to, the
        channel needs to already exist for the call to be successful.
        :param message: str, the actual message.
        :param botname: str, name of the bot that sends the message.
        :return:
        """
        channel = '#'+channel

        # is response an unused variable name ?
        response = self.client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message,
            as_user=False,
            username=botname
        )



# -----------  RETRIEVING TRANSACTION INFORMATION ----------------

VALUE_THRESHOLD = 1500

# Importing authentication token
with open("../../services/token.json") as datafile:
    data = json.load(datafile)
auth_token = data['token']

# Initialising the class
slack_util = SlackUtil(auth_token)

# retrieving top transactions from the last week

d = datetime.date.today()

currentObj = d - datetime.timedelta(days=0)
latest_date = currentObj.strftime('%Y-%-m-%d')

weekAgoObj = d - datetime.timedelta(days=7)
week_ago = weekAgoObj.strftime('%Y-%-m-%d')

s = get_top_transactions(week_ago, latest_date)

# Finding the highest value transaction and its corresponding address
max_value = s['Value'].max()
max_address = s[s['Value'] == s['Value'].max()]['Address']

address_str = str(max_address).split()[1][:-1]+')'

max_date = s[s['Value'] == s['Value'].max()]['Date']
date_str = str(max_date)[6:30]



# -----------   POSTING TO SLACK  -----------------------

# Post to slack only if transaction is big enough
if max_value > VALUE_THRESHOLD:
    slack_util.send_message('anova-blocksci', 'Biggest transaction in the last week', 'Zarif_bot')
    slack_util.send_message('anova-blocksci', 'Date: ' + date_str, 'Zarif_bot')
    slack_util.send_message('anova-blocksci', 'Value: ' + str(max_value), 'Zarif_bot')
    slack_util.send_message('anova-blocksci', 'Address: ' + address_str, 'Zarif_bot')
    FILE = open('logfile.txt', 'a')
    FILE.write('CURRENT DATE: ' + latest_date + '\n')
    FILE.write('Biggest transaction in the last week\n')
    FILE.write('Date: ' + date_str + '\n')
    FILE.write('Value: ' + str(max_value) + '\n')
    FILE.write('Address: ' + address_str + '\n')
    FILE.write("\n")


else:

    FILE = open('logfile.txt', 'a')
    FILE.write('CURRENT DATE: ' + latest_date + '\n')
    FILE.write('Balance has not changed significantly'+ '\n')
    FILE.write('Date: ' + date_str + '\n')
    FILE.write('Value: ' + str(max_value) + '\n')
    FILE.write('Address: ' + address_str + '\n')
    FILE.write("\n")

FILE.close()
