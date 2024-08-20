from flask import Flask, render_template

# Vars
app = Flask(__name__)


# Routes
@app.route("/", methods=["GET"])
def hello():
    return render_template("extend.html")
