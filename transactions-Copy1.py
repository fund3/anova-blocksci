import blocksci 
import numpy as np
import pandas as pd
import time

global CHAIN
CHAIN = blocksci.Blockchain("/home/ubuntu/bitcoin")

def get_spam(start, end):
    
    subchain = CHAIN.range(start=start, end=end)
    
    transactions = []
    for block in range(len(subchain)):
        #finds the value of outputs spent in a transaction (ie not the UTXOs)
        t = [(output.value, time.ctime(int(output.block.timestamp)),output.address)
             for output in subchain[block].txes.outputs if output.is_spent and output.value < 550]
        if(t): transactions.append(t)
            
            
    transactions = sum(transactions, [])
    df = pd.DataFrame(transactions, columns=['Value', 'Date', 'Address'])
    return len(df)

def get_top_transactions(start, end, threshold = 500):
    
    subchain = CHAIN.range(start=start, end=end)

    
    transactions = []
    for block in range(len(subchain)):
        #finds the value of outputs spent in a transaction (ie not the UTXOs)
        t = [(output.value/10e8, time.ctime(int(output.block.timestamp)),output.address)
             for output in subchain[block].txes.outputs if output.is_spent and output.value/10e8 > threshold]
        if(t): transactions.append(t)
            
            
    transactions = sum(transactions, [])
    df = pd.DataFrame(transactions, columns=['Value', 'Date', 'Address'])
    return df

