from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == '__init__':
    app.run()
