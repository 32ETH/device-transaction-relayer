#!/usr/bin/python3
import os
from brownie import LoggerNFT, accounts
from ..scripts import helpers
from dotenv import load_dotenv

load_dotenv()

device_account = accounts[0]
device_id = 1


def main():
    logger = os.getenv("PRIVATE_KEY")
    print(logger)
    # last_timestamp = helpers.last_timestamp(device_id)
    # fresh_data = helpers.load_database(last_timestamp)
    # helpers.record_to_blockchain(fresh_data)
