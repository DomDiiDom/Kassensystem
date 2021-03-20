import flask
import json

app = flask.Blueprint('Import', __name__, template_folder='templates')

@app.route("/js/<js>")
def js(js):
    return flask.send_file(f"static/js/{js}")
@app.route("/css/<css>")
def css(css):
    return flask.send_file(f"static/css/{css}")
@app.route("/css/<lib>/<css>")
def csslib(lib, css):
    return flask.send_file(f"static/css/{lib}/{css}")