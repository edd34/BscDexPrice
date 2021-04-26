// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './interfaces/IUniswapV2Router02.sol'

contract BscDexPrices {
    address private owner;
    constructor() {
        owner = msg.sender;
    }

    function swap(address dex1, address dex2, address tokenA, address tokenB) public returns(uint256) {
        
    }
}