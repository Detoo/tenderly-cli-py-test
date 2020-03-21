help:
	@egrep '^\w+:' Makefile

clean:
	rm -rf node_modules && rm -rf env

build_py_env:
	virtualenv -p python3.7 env

install_py_dependencies: build_py_env
	env/bin/pip install -r requirements.txt

install_node_dependencies:
	npm install

install_all_dependencies: install_py_dependencies install_node_dependencies

# Prerequisites: You must have truffle installed globally (ex. npm install -g truffle)
compile_contracts:
	truffle compile

# Make sure the network ID is added manually to your contract artifact json file; otherwise tenderly-cli proxy won't find be able to use it for debug tracing.
run_local_testnet:
	node_modules/.bin/ganache-cli --networkId=123456789

# Prerequisites: You must have tenderly installed globally (https://medium.com/tenderly/how-to-debug-solidity-smart-contracts-with-tenderly-and-truffle-da995cfe098f)
run_tenderly_proxy:
	tenderly proxy

# Run and behold the human-readable stack-trace.
run_py_app:
	env/bin/python py_utils/run.py
