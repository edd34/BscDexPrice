from web3 import Web3
class ContractUniswapClone:
    def __init__(self, address, abi, w3):
        self.address = address
        self.abi = abi
        self.w3 = w3
        self.contract = self.w3.eth.contract(address=self.address, abi=self.abi)
    
    def getEchangeRate(self, amount_in, address_token_a, address_token_b):
        return self.contract.functions.getAmountsOut(amount_in, [Web3.toChecksumAddress(address_token_a), Web3.toChecksumAddress(address_token_b)]).call()