from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

# In-memory storage for URLs
url_mapping = {}

# Function to generate a unique short code
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# URL Shortening Endpoint
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json.get("url")
    if not data:
        return jsonify({"error": "No URL provided"}), 400

    short_code = generate_short_code()
    short_url = f"http://192.168.56.102:5000/{short_code}"
    url_mapping[short_code] = data  # Store the mapping

    return jsonify({"short_url": short_url})

# URL Redirection Endpoint
@app.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({"error": "URL not found"}), 404

# Endpoint to retrieve original URL
@app.route('/get_original', methods=['POST'])
def get_original_url():
    data = request.json.get("short_code")
    if not data:
        return jsonify({"error": "No short code provided"}), 400

    # Extract the short code from the short URL (if provided)
    if data.startswith("http://192.168.56.102:5000/"):
        short_code = data.split("/")[-1]  # Extract the last part of the URL
    else:
        short_code = data  # Assume it's already the short code

    original_url = url_mapping.get(short_code)
    if original_url:
        return jsonify({"original_url": original_url})
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
