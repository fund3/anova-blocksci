#!/bin/bash

# Trying out writing a bash script

# directory to the file below is
# home/ubuntu/BlockSci/Notebooks/Zarif/postToSlack

cd /home/ubuntu/BlockSci/Notebooks/Zarif/postToSlack

python3 postToSlack.py
echo The slack.sh file is running




# The command below worked - to copy this file into cron.daily

# sudo cp /home/ubuntu/BlockSci/Notebooks/Zarif/postToSlack/slack.sh /etc/cron.daily/slack.sh