import pprint
from web3 import Web3, eth
import web3
from helpers.dex import dex
from helpers.Contract import ContractUniswapClone
from helpers.token import token_address

# ganache-cli -f https://bsc-dataseed1.binance.org -e 1000 -p 8546
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
Pancake = ContractUniswapClone(
    dex["pancakeswap"]["router_address"],
    dex["pancakeswap"]["abi"],
    w3,
    dex["pancakeswap"]["factory_address"],
    dex["pancakeswap"]["init_hash"],
)

Bscswap = ContractUniswapClone(
    dex["bscswap"]["router_address"],
    dex["pancakeswap"]["abi"],
    w3,
    dex["bscswap"]["factory_address"],
    dex["bscswap"]["init_hash"],
)

res1 = Pancake.getEchangeRate(10 ** 5, token_address["eth"], token_address["busdt"])
res2 = Bscswap.getEchangeRate(res1[1], token_address["busdt"], token_address["eth"])
print(res1, res2)

res3 = Bscswap.get_pair_address(token_address["busdt"], token_address["eth"])
print(res3.hex())