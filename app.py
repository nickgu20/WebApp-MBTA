"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=["GET", "POST"])
def index_post():
    if request.method =="POST":
        location = request.form["location"]
        # return location
        mbta, wheelchair = find_stop_near(location)
        if mbta != "No location found":
            return render_template("return.html", mbta=mbta, wheelchair=wheelchair)
        else:
            return render_template("error.html")


if __name__ == "__main__":
    app.run(debug= True)