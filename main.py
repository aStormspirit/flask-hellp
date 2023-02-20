from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello world!</p>"

app.run("0.0.0.0", 5000)