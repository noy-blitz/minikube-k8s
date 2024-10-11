from flask import Flask, jsonify

app = Flask(__name__)

# Flags for health and readiness
ready = True
healthy = True

# Health endpoint: always return 200 unless unhealthy
@app.route('/health', methods=['GET'])
def health_check():
    if healthy:
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500

# Readiness endpoint: Service-B is always ready, so return 200
@app.route('/ready', methods=['GET'])
def readiness_check():
    return jsonify({"status": "ready"}), 200

@app.route('/', methods=['GET'])
def hello_microsoft():
    return "Hello Microsoft!", 200

if __name__ == '__main__':
    # Start the Flask server
    app.run(host='0.0.0.0', port=8081)
