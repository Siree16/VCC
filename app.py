from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# URL Shortening Endpoint
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json.get("url")
    if not data:
        return jsonify({"error": "No URL provided"}), 400

    short_url = f"http://192.168.56.102:5000/abc123"  # Simulated short URL

    return jsonify({"short_url": short_url})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # ✅ Ensure Flask runs on all IPs
