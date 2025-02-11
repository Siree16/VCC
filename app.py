from flask import Flask, request, jsonify, redirect
import random
import string

app = Flask(__name__)

# Dictionary to store URL mappings
url_mapping = {}

def generate_short_code():
    """Generate a random 6-character short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# URL Shortening Endpoint
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json.get("url")
    if not data:
        return jsonify({"error": "No URL provided"}), 400

    # Generate a unique short code
    short_code = generate_short_code()
    while short_code in url_mapping:
        short_code = generate_short_code()

    url_mapping[short_code] = data

    return jsonify({"short_url": f"http://192.168.56.102:5000/{short_code}"})

# URL Redirect Endpoint
@app.route('/<short_code>', methods=['GET'])
def get_original_url(short_code):
    original_url = url_mapping.get(short_code)
    if not original_url:
        return jsonify({"error": "Short URL not found"}), 404

    return redirect(original_url, code=302)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
