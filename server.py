from flask import Flask, request, jsonify
import util  # Ensure util.py is in the same directory

app = Flask(__name__)

# Route to get all location names
@app.route('/get_location_names', methods=['GET'])  # Correct URL path
def get_location_names():
    try:
        locations = util.get_location_names()  # Call util.py function
        response = jsonify({
            'locations': locations
        })
        response.headers.add('Access-Control-Allow-Origin', '*')  # CORS
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to predict home price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Ensure all required form data is present
        total_sqft = float(request.form.get('total_sqft', 0))
        location = request.form.get('location', '').strip()
        bhk = int(request.form.get('bhk', 0))
        bath = int(request.form.get('bath', 0))

        # Validate input
        if not location or total_sqft <= 0 or bhk <= 0 or bath <= 0:
            return jsonify({'error': 'Invalid input data'}), 400

        # Call util.py function for prediction
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')  # CORS
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True)  # Debug mode for detailed error messages
