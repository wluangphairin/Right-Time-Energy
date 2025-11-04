from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/status")
def status():
    return jsonify({
        "status": "Server running",
        "price": 10.42   # example value in ¢/kWh
    })

if __name__ == "__main__":
    app.run(debug=True)
