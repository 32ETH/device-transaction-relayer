// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;


// A simple contract that allows any users to store a message in the graffity
// contract the contract only stores one message, so when a message is stored it over 
// writes the previous message.
// its important to note, this contract, and every other contract on chain only knows
// about the data in this contract, however because a event is emitted every time the
// message is changed, it is possible to get the history of all the messages from the
// ethereum logs
contract Graffity {
    string public message;

    // @notice Store the new message with the writers address
    event MessageChanged(string message, address sender);

    constructor(string _message) public {
        message = _message;
    }

    // @notice Store the new message with the writers address
    function setMessage(string _message) public {
        message = _message;
        emit MessageChanged(message);
    }
}