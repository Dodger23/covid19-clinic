from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)


@app.route("/")
def mod():
        return render_template('model.html')


url = 'http://3f6dc8ccaebe.ngrok.io/predict'
@app.route('/predict', methods=['GET', 'POST'])
@app.route("/")
def predict():
#     files = request.files.getlist('uploadFile')
    if request.method == 'POST':
        file = request.files['uploadFile']
        if file:
                r = requests.post(url, files={'file':file})

    return render_template('model.html', message=r.json()['predicted_class'])

        
app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == '__main__':
    app.run()
