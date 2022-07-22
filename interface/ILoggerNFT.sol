// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

interface ILoggerNFT is ERC721, Ownable {
    mapping(address => uint) public loggers;
    mapping(uint => uint) public lastTimestamp;

    struct Data {
        uint256 temprature;
        string gps;
        uint timestamp;
    }

    event LogData(uint loggerId, Data data);
    event LoggerAdded(address logger, uint loggerId);

    constructor() ERC721("BlockPharm Logger", "LOGGER") {}

    function addLogger(address logger, address owner) public onlyOwner;
    function logData(
        uint loggerId,
        uint temp,
        string calldata gps,
        uint calldata timestamp
    ) public;
    function numOfLoggers() public view returns (uint);
}