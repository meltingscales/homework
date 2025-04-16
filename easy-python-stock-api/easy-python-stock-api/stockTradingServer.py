from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

# Define the seeded data for each stock
seed_data = {
    'TSLA': [100.0, 105.0, 102.5, 101.8],
    'AAPL': [150.0, 155.0, 153.2, 151.3],
    'PYTHN': [200.0, 205.0, 202.5, 201.8]
}

# Define the stock endpoint
@app.route('/stock/<string:symbol>', methods=['GET'])
def get_stock(symbol):
    if symbol in seed_data:
        return jsonify({symbol: seed_data[symbol]})
    else:
        return jsonify({'message': f'Stock {symbol} not found.', "validRoutes": (list(seed_data.keys()))})

# In case they visit us
@app.route("/")
def index():
    return jsonify({
        "message": "Hello! This is the stock trading server. Welcome.",
        "routes": [("/stock/" + sym) for sym in (list(seed_data.keys()))],
    })

# Run the server
if __name__ == '__main__':
    app.run(host='localhost', port=8000)
