## Debug Solidity Smart Contracts with Tenderly and Truffle using Python

### Global Environment Prerequisites

* [`virtualenv`](https://pypi.org/project/virtualenv/)
* [`truffle`](https://www.trufflesuite.com/docs/truffle/getting-started/installation)
* [`tenderly-cli`](https://github.com/Tenderly/tenderly-cli)

### Setup Local Environment

```shell script
make install_all_dependencies
```

### Run Ganache Testnet and Tenderly Proxy

Run the following scripts in two separate sessions (they will be running in the foreground):
```shell script
make run_local_testnet
```
```shell script
make run_tenderly_proxy
```

### Run Tests and Verify Results

```shell script
make run_tests
```
