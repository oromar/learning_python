from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:number>', methods=['GET'])
def hello(number):
    return jsonify({'message':'Hello World {}'.format(number)})

if __name__ == '__main__':
    app.run(debug=True)

