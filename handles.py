from flask import jsonify, request
from settings import w3, app
from app_service import get_balance, get_top_addresses, get_top_with_transactions, get_token_info


@app.route('/get_balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "Invalid address"}), 400
    
    balance = get_balance(address)

    return jsonify({"balance": str(balance)})


@app.route('/get_balance_batch', methods=['POST'])
def get_balance_batch():
    addresses = request.json.get('addresses', [])
    if not addresses:
        return jsonify({"error": "No addresses provided"}), 400

    balances = []
    for address in addresses:
        if not address:
            return jsonify({"error": "Invalid address"}), 400
        balance = get_balance(address)
        balances.append(float(balance))

    return jsonify({"balances": balances})


@app.route('/get_top', methods=['GET'])
def get_top():
    n = request.args.get('n', type=int)
    if not n:
        return jsonify({"error": "Parameter 'n' is required"}), 400
    top_addresses = get_top_addresses(n)

    return jsonify({"top_addresses": top_addresses})


@app.route('/get_top_with_transactions', methods=['GET'])
def api_get_top_with_transactions():
    n = request.args.get('n', type=int)
    if not n:
        return jsonify({"error": "Parameter 'n' is required"}), 400
    top_addresses = get_top_with_transactions(n)

    return jsonify({"top_addresses": top_addresses})


@app.route('/get_token_info', methods=['GET'])
def api_get_token_info():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "Token address is required"}), 400
    token_info = get_token_info(address)
    return jsonify(token_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

