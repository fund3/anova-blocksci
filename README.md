# anova-blocksci

This is a service that notifies significant changes in cryptocurrency transactions and spam transactions,
with the notifications being sent as Slack messages to a specific channel #anova-blocksci

## Dependencies

Python3, pandas, numpy, blocksci, json, datetime

## Getting Started

All the important files are in the /postToSlack folder, and they are as follows:

post_to_slack.py
slack.sh
logfile.txt

# How it works:

- the bash script 'slack.sh' is run every 6 hours through cronjob 
This is achieved by copying the file into /etc/cron.daily/slack.sh

- the bash script runs 'post_to_slack.py' which does all the heavy-lifting. It analyses recent crypto
transactions and sends a notification to slack depending on whether the transactions exceeded threshold values

- A summary of the transactions found is written to 'logfile.txt' regardless of whether they were big
enough to be posted on Slack

