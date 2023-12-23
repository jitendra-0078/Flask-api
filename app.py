# Import necessary modules from Flask framework
from flask import Flask, jsonify, request

# Import the gcd function from the math module
from math import gcd

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the Healthcheck endpoint
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    # Return a JSON response indicating "Healthy" and a status code of 200
    return jsonify({"status": "Healthy"}), 200

# Define a route for the GCD endpoint
@app.route('/gcd', methods=['POST'])
def calculate_gcd():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract values of 'x' and 'y' from the JSON data
    x = data.get('x')
    y = data.get('y')

    # Check if both 'x' and 'y' are provided in the JSON data
    if x is None or y is None:
        return jsonify({"error": "Invalid input. Both 'x' and 'y' must be provided."}), 400

    try:
        # Attempt to convert 'x' and 'y' to integers
        x = int(x)
        y = int(y)
    except ValueError:
        # Handle the case where 'x' or 'y' is not a valid integer
        return jsonify({"error": "Invalid input. 'x' and 'y' must be integers."}), 400

    # Calculate the GCD of 'x' and 'y' using the gcd function
    result = gcd(x, y)

    # Return the result as a JSON response with a status code of 200
    return jsonify({"result": result}), 200

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
