"""
Simple Util class to send a slack message notification.
"""
from slackclient import SlackClient
import json
from pprint import pprint

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
        channel = '#' + channel
        # TODO(calvinleungyk): Find a way to handle or log the response.
        response = self.client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message,
            as_user=False,
            username=botname
        )
       
        

# CALLING STARTS BELOW

# Importing authentication token 
with open("../../services/token.json") as datafile:
    data = json.load(datafile)
auth_token = data['token']

# Initialising the class
slack_util = SlackUtil(auth_token)

balanceChanged = True

# Post to slack only if balance has changed significantly
if balanceChanged:
    
    slack_util.send_message('anova-blocksci', 'Test message.', 'Zarif_bot')
    file = open('testfile.txt', 'w') 
    file.write('Balance has changed!')
    
else:
    
    file = open('testfile.txt', 'w') 
    file.write('Balance has not changed') 
    
file.close() 





