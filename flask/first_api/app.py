from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def my_api(id):
    return jsonify({'id': id, 'name':'Oromar', 'occupation':'Software Engineer'})

# @app.route('/sum/<int:val1>/<int:val2>')
# def sum(val1, val2):
#     return jsonify({'sum':val1+val2})

@app.route('/sum', methods=['POST','PUT'])
def my_sum():
    data = json.loads(request.data)
    total = sum(data['values'])
    return {'sum': total}

if __name__ == '__main__':
    app.run(debug=True)

