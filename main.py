from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/model")
def mod():
        return render_template('model.html')

@app.route("/about_us")
def about():
        return render_template('about_us.html')


#@app.route("/predict")
#def predict():

        
app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == '__main__':
    app.run()
