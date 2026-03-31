from flask import Flask, render_template, request, jsonify
import hashlib
import random
import os

# Initialize Flask App
app = Flask(__name__)

# Simulated blockchain storage
blockchain = {}

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/before', methods=['POST'])
def before():
    data = request.json['data']
    # No protection → always "accepted"
    return jsonify({
        "message": "⚠️ Data accepted without verification (Vulnerable System)"
    })

@app.route('/after_generate', methods=['POST'])
def after_generate():
    data = request.json['data']
    h = generate_hash(data)
    blockchain['hash'] = h
    return jsonify({
        "hash": h,
        "message": "✅ Proof Generated and Stored (Simulated Blockchain)"
    })

@app.route('/iot_data', methods=['GET'])
def iot_data():
    samples = [
        "Patient Heart Rate: 72 bpm",
        "Temperature Sensor: 28°C",
        "Traffic Density: Moderate",
        "Air Quality Index: Good",
        "Machine Status: Normal"
    ]
    return jsonify({"data": random.choice(samples)})

@app.route('/after_verify', methods=['POST'])
def after_verify():
    data = request.json['data']
    new_hash = generate_hash(data)

    if blockchain.get('hash') == new_hash:
        return jsonify({
            "status": "verified",
            "message": "✅ Verified: Data is authentic"
        })
    else:
        return jsonify({
            "status": "tampered",
            "message": "❌ Tampered: Data has been modified"
        })

if __name__ == '__main__':
    # Render binds the port via an environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)