from flask import Flask, request, jsonify, redirect
from flask_cors import CORS  # ✅ Import CORS

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# Simulated in-memory storage for short URLs
short_url_mapping = {
    "abc123": "https://www.google.com",  # Example short URL to original URL mapping
}

# URL Shortening Endpoint
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json.get("url")
    if not data:
        return jsonify({"error": "No URL provided"}), 400

    # Generate a simulated short URL (this would usually be dynamic)
    short_url = f"http://192.168.56.102:5000/abc123"  # Simulated short URL
    return jsonify({"short_url": short_url})

# Endpoint to retrieve the original URL from a short URL code
@app.route('/<short_code>', methods=['GET'])
def get_original_url(short_code):
    # Check if the short URL code exists in the mapping
    original_url = short_url_mapping.get(short_code)
    if not original_url:
        return jsonify({"error": "Short URL not found"}), 404

    # Redirect to the original URL
    return redirect(original_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # ✅ Ensure Flask runs on all IPs
