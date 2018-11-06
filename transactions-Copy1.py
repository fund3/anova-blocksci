"""Module for output of slack scripts"""

import blocksci 
import numpy as np
import pandas as pd
import time

global CHAIN
CHAIN = blocksci.Blockchain("/home/ubuntu/bitcoin")

def get_spam(start, end):
    """
    returns distribution of transactions where fees are below 6 satoshis per byte
    
    start, end: timestamps
    """
    
    subchain = chain.range(start=start, end=end)
    
    transactions = []
    for block in range(len(subchain)):
        average_fee = subchain[block].fee / len(subchain[block]) 
        
        t = [(tx.fee, average_fee,(tx.fee/average_fee)*100,tx.fee_per_byte(),  time.ctime(subchain[block].timestamp)) for tx in subchain[block].txes if tx.fee_per_byte()  <= 6 and tx.fee > 0]
        if(t): transactions.append(t)
            
    transactions = sum(transactions, [])
    df = pd.DataFrame(transactions, columns=['Tx_Fee', 'Average_Fee','Pcnt_of_average_fee' ,'Fee_per_byte', 'Time'])
    
    
    return df.describe().round(2)

def get_top_transactions(start, end, threshold = 2000):
    """
    returns all transactions obove threshold for period. Gives output address (if unspent), value and date
    
    start, end: timestamps
    threshold: btc value
    """
    
    subchain = chain.range(start=start, end=end)
    
    transactions = []
    for block in range(len(subchain)):
        t = [(output.value/10e7, time.ctime(int(output.block.timestamp)),output.address)
             for output in subchain[block].txes.outputs if output.value/10e7 > threshold and output.is_spent == False]
        if(t): transactions.append(t)
            
            
    transactions = sum(transactions, [])
    df = pd.DataFrame(transactions, columns=['Value', 'Date', 'Output Address'])
    return df
