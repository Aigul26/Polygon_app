from settings import contract, w3, TOKEN, POLYGON_RPC
import requests


def get_balance(address):
    balance = contract.functions.balanceOf(address).call()
    return w3.from_wei(balance, 'ether')

def get_top_addresses(n):
    url = f"https://api.polygonscan.com/api?module=token&action=tokenholderlist&contractaddress={TOKEN}&page=1&offset={n}&apikey={POLYGON_RPC}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['status'] == '1':
            top_addresses = [(holder['address'], holder['balance']) for holder in data['result']]
            return top_addresses
        else:
            print(f"Error: {data['message']}")
            return 
    else:
        print(f"HTTP Error: {response.status_code}")
        return 
    
def get_top_with_transactions(n):
    url = f"https://api.polygonscan.com/api?module=token&action=tokenholderlist&contractaddress={TOKEN}&page=1&offset={n}&apikey={POLYGON_RPC}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        top_addresses = data['result'][:n]
        result = []

        for address in top_addresses:
            balance = contract.functions.balanceOf(address).call()
            decimals = contract.functions.decimals().call()
            balance_normalized = balance / (10 ** decimals)

            tx_url = f"https://api.polygonscan.com/api?module=account&action=txlist&address={address}&sort=desc&apikey=YOUR_API_KEY"
            tx_response = requests.get(tx_url)
            tx_data = tx_response.json()
            last_transaction_date = tx_data['result'][0]['timeStamp'] if tx_data['result'] else "none"

            result.append((address, balance_normalized, last_transaction_date))

        return result
    else:
        print(f"HTTP Error: {response.status_code}")
        return 
    
def get_token_info(address):

    symbol = contract.functions.symbol().call()
    name = contract.functions.name().call()
    total_supply = contract.functions.totalSupply().call()
    decimals = contract.functions.decimals().call()
    return {
        'symbol': symbol,
        'name': name,
        'totalSupply': total_supply / (10 ** decimals)
    }

    
