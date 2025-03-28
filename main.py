import json
from flask import Flask, jsonify
from werkzeug.exceptions import NotFound, BadRequest
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app


# Load package data from the JSON file
def load_packages():
    with open("packages.json", "r") as f:
        return json.load(f)


# Error handler for 404 errors
@app.errorhandler(NotFound)
def not_found_error(error):
    return jsonify({"code": "404", "message": "Not Found"}), 404


# Error handler for 400 errors
@app.errorhandler(BadRequest)
def bad_request_error(error):
    return jsonify({"code": "400", "message": str(error)}), 400


@app.route("/packages/<int:packageId>", methods=["GET"])
def get_package(packageId):
    """
    Gets package information from packages.json given the packageId (product_id).
    """
    packages = load_packages()
    package = packages.get(str(packageId))
    if package:
        return jsonify(package), 200
    else:
        raise NotFound(f"Package with id {packageId} not found")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
