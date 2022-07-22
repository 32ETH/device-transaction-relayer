import os
from brownie import Graffity, accounts
import pandas as pd
from web3 import Web3
from pprint import pprint

pp = pprint


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


def get_logger_history(graffity):
    contract = w3.eth.contract(address=graffity.address, abi=graffity.abi)

    # get the events from the contract
    filter = contract.events.MessageChanged.createFilter(fromBlock=0)
    events = filter.get_all_entries()

    # create a dataframe from the events
    mappedList = map(lambda d: [d.args["message"], d.args["sender"]], events)
    df = pd.DataFrame(list(mappedList), columns=["MESSAGE", "WRITER"])
    return df
