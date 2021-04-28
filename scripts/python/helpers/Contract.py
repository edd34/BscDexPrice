from eth_abi.packed import encode_abi_packed

from web3 import Web3
class ContractUniswapClone:
    def __init__(self, router_address, abi, w3, factory_address, init_hash):
        self.router_address = router_address
        self.abi = abi
        self.w3 = w3
        self.router_contract = self.w3.eth.contract(address=self.router_address, abi=self.abi)
        self.factory_address = factory_address
        self.init_hash = init_hash
    
    def getEchangeRate(self, amount_in, address_token_a, address_token_b):
        return self.router_contract.functions.getAmountsOut(amount_in, [Web3.toChecksumAddress(address_token_a), Web3.toChecksumAddress(address_token_b)]).call()
    
    def get_pair_address(self, token1, token2):
        abiEncoded_1 = encode_abi_packed(['address', 'address'], tuple(sorted((token1, token2))))
        salt_ = self.w3.solidityKeccak(['bytes'], ['0x' +abiEncoded_1.hex()])
        abiEncoded_2 = encode_abi_packed([ 'address', 'bytes32'], ( self.factory_address, salt_))
        resPair = self.w3.solidityKeccak(['bytes','bytes'], ['0xff' + abiEncoded_2.hex(), self.init_hash])[12:]
        return resPair