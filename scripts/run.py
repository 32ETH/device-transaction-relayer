#!/usr/bin/python3
import os
from brownie import LoggerNFT, accounts
from ..scripts import helpers
import json

device_account = accounts[0]
device_id = 1


def main():
    logger = helpers.get_device_wallet()
    print(f"Device Address: {logger.address}")
    last_timestamp = helpers.last_timestamp(device_id)
    print(f"last_timestamp: {last_timestamp}")
    # fresh_data = helpers.load_database(last_timestamp)
    # helpers.record_to_blockchain(fresh_data)
