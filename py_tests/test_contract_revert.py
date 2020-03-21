import pytest
import json
from web3 import Web3, HTTPProvider


def test_revert_should_have_readable_stack_trace():

    web3 = Web3(HTTPProvider('http://localhost:9545'))  # Tenderly proxy
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Deploy contract.
    calculator_build = json.load(open('build/contracts/Calculator.json', 'r'))
    calculator_contract = web3.eth.contract(abi=calculator_build['abi'], bytecode=calculator_build['bytecode'][2:])
    tx_hash = calculator_contract.constructor().transact()
    calculator_address = web3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    calculator = web3.eth.contract(abi=calculator_build['abi'])(address=calculator_address)

    # Test and verify.
    with pytest.raises(ValueError) as revert_info:
        # Specify gas so it does not try to estimate it and raise exception before sending TX.
        calculator.functions.div(10**18, 0).transact({'gas': 10**6})
    assert('c = a / b' in revert_info.value.args[0]['message'])
