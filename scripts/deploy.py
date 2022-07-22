#!/usr/bin/python3
from brownie import Graffity, accounts
from . import helpers

deployer_account = accounts[0]
# abdullah = accounts[1]
# usama = accounts[2]
# raj = accounts[3]


def main():
    wall = Graffity.deploy("A Nice clean wall", {"from": accounts[0]})
    lastMessage = wall.message()
    print(f"\nOn the wall: {lastMessage}")

    # wall.setMessage("Abdullah was here!", {"from": abdullah})
    # wall.setMessage("Usama was here!", {"from": usama})
    # wall.setMessage("Raj was here!", {"from": raj})

    # lastMessage = wall.message()
    # print(f"\nOn the wall: {lastMessage}\n")

    # history = helpers.get_logger_history(wall)
    # print("-------------------------- Wall History -------------------------")
    # print(history)
