import pprint
from web3 import Web3, eth
import web3
from helpers.dex import dex
from helpers.Contract import ContractUniswapClone
from helpers.token import token_address

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
Pancake = ContractUniswapClone(
    dex["pancakeswap"]["token"], dex["pancakeswap"]["abi"], w3
)

Bscswap = ContractUniswapClone(
    dex["bscswap"]["token"], dex["pancakeswap"]["abi"], w3
)

res1 = Pancake.getEchangeRate(10**5, token_address["eth"], token_address["busdt"])
res2 = Bscswap.getEchangeRate(res1[1], token_address["busdt"], token_address["eth"])
print(res1, res2)
