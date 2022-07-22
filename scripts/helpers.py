import os
from brownie import LoggerNFT, accounts, Contract
import pandas as pd
from web3 import Web3
from dotenv import load_dotenv
import json


load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


def get_device_wallet():
    return accounts.add(os.getenv("PRIVATE_KEY"))


def get_logger_contract():
    abi = json.load(open("build/contracts/LoggerNFT.json", "r"))["abi"]
    return Contract.from_abi("LoggerNFT", os.getenv("LOGGER_ADDRESS"), abi)


def last_timestamp(device_id):
    loggerNFT = get_logger_contract()
    return loggerNFT.timestamp(device_id)


def get_logger_history(loggerNFT, id):
    contract = w3.eth.contract(address=loggerNFT.address, abi=loggerNFT.abi)

    # get the events from the contract
    filter = contract.events.LogData.createFilter(
        fromBlock=0, arguments={"loggerId": id}
    )
    events = filter.get_all_entries()

    # create a dataframe from the events
    mappedList = map(lambda d: d.args.data, events)
    df = pd.DataFrame(list(mappedList), columns=["temp", "gps", "timestamp"])
    return df
