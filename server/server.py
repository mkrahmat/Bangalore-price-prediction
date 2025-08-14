import os
from flask import Flask, request, jsonify, send_from_directory
import util

BASE_DIR = os.path.dirname(__file__)
CLIENT_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "client"))

app = Flask(__name__, static_folder=CLIENT_FOLDER, static_url_path='')

@app.route('/')
def index():
    return send_from_directory(CLIENT_FOLDER, 'app.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(CLIENT_FOLDER, filename)

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names_api():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price_api():
    total_sqft = float(request.form.get('total_sqft', 0))
    location = request.form.get('location', '')
    bhk = int(request.form.get('bhk', 0))
    bath = int(request.form.get('bath', 0))

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    response = jsonify({'estimated_price': estimated_price})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
