import json
from flask import Flask, jsonify, abort
from werkzeug.exceptions import NotFound

app = Flask(__name__)

# create /discovery /readiness /liveness routes
@app.route('/discovery', methods=['GET'])
def discovery():
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live"})

@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready"})




if __name__ == "__main__":
    app.run(debug=True, port=5001)
