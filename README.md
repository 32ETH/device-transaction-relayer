# Device Transaction Relayer

[![Codespaces Prebuilds](https://github.com/32ETH/device-transaction-relayer/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/32ETH/device-transaction-relayer/actions/workflows/codespaces/create_codespaces_prebuilds)

The program is designed to run directly on the device, it assumes the logging program is storing logging data to a local database (a local `data.json` file). The `Device Transaction Relayer` runs on a cron job every minute and does the following:

1. Queries the LoggerNFT contract for the last datapoint and extracts the timestamp
2. Imports the local `data.json` and returns an array of the latest datapoints
3. Maps over the latest data points and for each datapoint: 4. calls the `LoggerNFT`'s `logData()` function

<br>

## Project Setup

We use codespaces to ensure the environment is easy to set up and deterministic

1. Visit the [repo here](https://github.com/32ETH/device-transaction-relayer)
2. Click the green "Code" button
3. Click "Create codespace on main"
4. Wait for the machine to setup
5. In the terminal run `brownie run scripts/deploy.py --silent`

<br>

## `./run.py`

> implimentation of the functions is stored in the `./helpers.py` file to keep the code clean and focus on whats happening rather than how

The code for the main file is very simple. When the program runs, it calls three functions, inputting the data returned from the previous step

<br>

```python=
#!/usr/bin/python3
from brownie import LoggerNFT, accounts
from . import helpers

device_account = accounts[0]
device_id = 1

main():
    last_timestamp = helpers.last_timestamp(device_id)
    fresh_data = helpers.load_database(timestamp)
    helpers.record_to_blockchain(fresh_data)

```

<br>

## `helpers.py`

#### `last_timestamp(device_id):`

> **_Returns_**: last timestamp

1. This function checks the last recorded timestamp for this device on the `LoggerNFT` contract
2. Then returns it

#### `load_database(timestamp):`

> **_Returns_**: the data since `timestamp` in a pandas dataframe

1. This function loads data from a local database. in production we would use SQL, but for the tech demo, the data will be saved into a json file in the home directory.
2. Then compares the `timestamp` with it the data its loacreates a dataframe with the
3. Then creates a dataframe with the fresh data
4. Then returns the fresh data

#### `record_to_blockchain():`

1. This function loops through the dataframe, for each entry:
    - calls `send_transaction(temp, location, timestamp)`

#### `send_transaction(temp, location, timestamp):`

1. This function calls the `logData(temp, location timestamp)` on the `LoggerNFT` contract


<br>

## Todo

-   [ ] function: `last_timestamp():`
-   [ ] function: `load_database():`
-   [ ] function: `record_to_blockchain():`
-   [ ] function: `send_transaction():`
