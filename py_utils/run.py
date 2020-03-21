import json
from web3 import Web3, HTTPProvider

import logging
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    import sys

    logging.basicConfig(
        format='%(asctime)-15s %(levelname)-8s %(message)s',
        level=logging.INFO,
        stream=sys.stdout,
    )

    web3 = Web3(HTTPProvider('http://localhost:9545'))  # Tenderly proxy
    web3.eth.defaultAccount = '0x9596C16D7bF9323265C2F2E22f43e6c80eB3d943'

    # Deploy contract.
    calculator_build = json.load(open('build/contracts/Calculator.json', 'r'))
    calculator_contract = web3.eth.contract(abi=calculator_build['abi'], bytecode=calculator_build['bytecode'][2:])
    tx_hash = calculator_contract.constructor().transact()
    calculator_address = web3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    calculator = web3.eth.contract(abi=calculator_build['abi'])(address=calculator_address)

    # Test.
    # Specify gas so it does not try to estimate it and raise exception before sending TX.
    calculator.functions.div(10**18, 0).transact({'gas': 10**6})
