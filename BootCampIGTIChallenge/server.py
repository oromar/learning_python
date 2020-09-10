from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)


def predict_diabets(form):
    pred = np.array(form).reshape(1, 8)
    model = joblib.load('melhor_modelo.sav')
    result = model.predict(pred)
    return result[0]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        list_form = request.form.to_dict()
        list_form = list(list_form.values())
        list_form = list(map(float, list_form))
        res = predict_diabets(list_form)
        if int(res) == 1:
            predict = 'Tem diabetes!'
        else:
            predict = 'Não tem diabetes!'
        return render_template('result.html', predict=predict)


if __name__ == '__main__':
    app.run(debug=True)
