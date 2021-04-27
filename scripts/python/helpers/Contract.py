class ContractUniswapClone:
    def __init__(self, address, abi, w3):
        self.address = address
        self.abi = abi
        self.w3 = w3
        self.contract = self.w3.eth.contract(address=self.address, abi=self.abi)
    
    def getEchangeRate(address_token_a, address_token_b):
        return self.contract.functions.getAmountsOut(address_token_a, [address_token_b])