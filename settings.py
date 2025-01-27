from web3 import Web3
from flask import Flask

app = Flask(__name__)

POLYGON_RPC = "https://polygon-rpc.com"
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))

TOKEN = Web3.to_checksum_address("0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0")

ERC20 = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

contract = w3.eth.contract(address=TOKEN, abi=ERC20)
