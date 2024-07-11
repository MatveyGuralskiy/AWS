from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/help")
def help():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
