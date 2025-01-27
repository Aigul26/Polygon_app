from web3 import Web3
from flask import Flask
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

POLYGON_RPC = "https://polygon-rpc.com"
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))



TOKEN = Web3.to_checksum_address(os.getenv('TOKEN_ADRESS'))

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
