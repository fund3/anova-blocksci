# test_post_to_slack.py

import pytest
import sys
import json
import blocksci
import numpy as np
import pandas as pd
import datetime

#from Zarif.postToSlack.post_to_slack import SlackUtil, failedPost

sys.path.append("../../")

from Zarif.postToSlack import post_to_slack
from services.transactions import get_top_transactions


def test_auth_token_received():
    with open("../../services/token.json") as datafile:
        data = json.load(datafile)
    auth_token = data['token']
    
    assert isinstance(auth_token, str)
    
def test_transactions_received():
    
    start_date = "2018-10-10"
    latest_date = "2018-10-15"
    
    s = get_top_transactions(start_date, latest_date)
    
    assert isinstance(s, pd.DataFrame)
