from flask import Flask, request, jsonify
import util  # Humne jo util.py banayi hai, use import kar rahe hain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. Location Names get karne ke liye endpoint
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# 2. UI se inputs lekar price predict karne ke liye endpoint
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # HTML form ya Postman se data receive karna
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # util.py ke function ko call karke prediction nikalna
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Server start hote hi model aur columns load ho jayenge
    app.run(port=5000, debug=True)