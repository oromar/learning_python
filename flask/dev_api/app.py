from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'It´s work!'})

if __name__ == '__main__':
    app.run(debug=True)