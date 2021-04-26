// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

// import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import '@openzeppelin/contracts/token/ERC20/IERC20.sol';
import "./IUniswapV2Router02.sol";
import "./IKyberNetworkProxy.sol";
import "@nomiclabs/buidler/console.sol";

contract Swap {
    address public uniswapAddress = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;
    address public kyberAddress = 0x818E6FECD516Ecc3849DAf6845e3EC868087B755;

    receive() external payable {}

    function HelloWorld() external view returns (string memory) {
        return "Hello world";
    }

    function runSwap(
        uint256 amount,
        address srcAddress,
        address dstAddress
    ) external {
        require(
            amount <= address(this).balance,
            "Not enough Eth in contract to perform swap."
        );
        IKyberNetworkProxy kyber = IKyberNetworkProxy(kyberAddress);
        IERC20 srcToken = IERC20(srcAddress);
        IERC20 dstToken = IERC20(dstAddress);

        // send amount to current smartcontract
        srcToken.approve(address(this), 0);
        srcToken.approve(address(this), amount);
        (uint256 rate, ) = kyber.getExpectedRate(srcToken, dstToken, amount);
        kyber.swapTokenToToken(srcToken, amount, dstToken, rate);
    }
}
