#!/usr/bin/python3

from brownie import Graffity, accounts

deployer_account = accounts[0]
abdullah = accounts[1]
usama = accounts[2]


def main():
    return Graffity.deploy("A Nice clean wall", {'from': accounts[0]})
