import requests
import time
from statistics import mean
from flask import Flask, jsonify
import threading

app = Flask(__name__)

# Flags to simulate readiness and health
ready = False
healthy = True

prices = []

# Function to fetch Bitcoin price from the API
def fetch_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    return response.json()['bpi']['USD']['rate_float']

# Function to continuously fetch the Bitcoin price and print the average
def start_bitcoin_fetching():
    global ready
    time.sleep(10)  # Simulate some initialization time before the service becomes "ready"
    ready = True  # Now the service is ready

    while True:
        try:
            price = fetch_bitcoin_price()
            print(f"Bitcoin Price: ${price}")
            prices.append(price)

            if len(prices) >= 10:
                avg_price = mean(prices[-10:])
                print(f"Average Bitcoin Price (last 10 minutes): ${avg_price}")

        except Exception as e:
            print(f"Error fetching Bitcoin price: {e}")
            healthy = False  # Mark service unhealthy if there's an error

        time.sleep(60)  # Fetch price every minute

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    if healthy:
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500

# Readiness check endpoint
@app.route('/ready', methods=['GET'])
def readiness_check():
    if ready:
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "not ready"}), 503


# Endpoint to fetch current Bitcoin price
@app.route('/price', methods=['GET'])
def get_price():
    if prices:  # Check if there's at least one price recorded
        current_price = prices[-1]  # Get the last recorded price
        return jsonify({"Bitcoin Price": current_price}), 200
    else:
        return jsonify({"error": "No price data available."}), 404

# Endpoint to fetch average Bitcoin price over the last 10 entries
@app.route('/average', methods=['GET'])
def get_average():
    if len(prices) < 10:
        return jsonify({"Average Price": "Not enough data to calculate average."}), 400
    avg_price = mean(prices[-10:])
    return jsonify({"Average Bitcoin Price (last 10 entries)": avg_price}), 200



if __name__ == '__main__':
    # Start the Bitcoin fetching process in a background thread
    threading.Thread(target=start_bitcoin_fetching).start()

    # Start the Flask server
    app.run(host='0.0.0.0', port=8080)
