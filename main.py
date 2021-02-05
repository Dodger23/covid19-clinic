from flask import Flask, request, redirect, render_template


app = Flask(__name__)

app.secret_key = "counter=0"

# a route where we will display a welcome message via an HTML template

message = "Home"


@app.route("/")
def index():
    return render_template('home.html', message="Home")


app.config["TEMPLATES_AUTO_RELOAD"] = True

# url = 'http://7633916b5988.ngrok.io/predict'
# @app.route('/predict', methods=['GET', 'POST'])
# @app.route("/model")
# def predict():
#     chk = requests.get(url).status_code
#     if chk == 404:
#         return render_template('model.html', message="404")
#     files = request.files.getlist('uploadFile')
#     pred = {}
#     if len(files) > 10:
#         return redirect('/model')

#     for file in files:
#         img = Image.open(file)
#         img = img.resize((256, 256))
#         buffered = BytesIO()
#         img.save(buffered, format="PNG")
#         pim = base64.b64encode(buffered.getvalue())
#         j = {"img": str(pim)}
#         r = requests.post(url, json=json.dumps(j)).json()
#         print(r)
#         res = r["pred"]
#         res = res.split()
#         res[1] = float(res[1])*100.0
#         if res[1] < 95:
#             res[0] = "What ?!!"
#         pred[str(pim)[2:-1]] = res[0]

#     return render_template('model.html', message=pred)


if __name__ == '__main__':
    app.run()
