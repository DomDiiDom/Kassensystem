import flask
import requests
import json
import Import
import Functions

app = flask.Flask(__name__)
app.register_blueprint(Import.app)
app.register_blueprint(Functions.app)

@app.route("/")
def index():
    return flask.render_template("content/index.html")

@app.route("/datenschutz")
def datenschutz():
    return flask.render_template("content/datenschutz.html")

@app.route("/impressum")
def impressum():
    return flask.render_template("content/impressum.html")

def sendRequest(url, method, data):
    request = requests.post(url + method, data)
    return request

if __name__ == "__main__":
    app.run(port=5000)
