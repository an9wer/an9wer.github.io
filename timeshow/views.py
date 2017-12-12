from bottle import Bottle, static_file

app = Bottle()

@app.route("/")
def index():
    return static_file("timeshow.html", root="./timeshow/templates/")

@app.route("/static/<path:path>")
def static(path):
    return static_file(path, root="./timeshow/static/")

@app.route("/api/load/")
def load():
    return {
        "items": [
            {"datetime": "2017-11-26", "mind": "I'll get it" },
            {"datetime": "2017-11-30", "mind": "demo it."},
            {"datetime": "2017-12-03", "mind": "dame cool."},
            {"datetime": "2017-12-05", "mind": "scroll to bottom load more"},
            {"datetime": "2017-12-07", "mind": "css transition"},
            {"datetime": "2017-12-08", "mind": "ease loading"},
            {"datetime": "2017-12-10", "mind": "transform"},
            {"datetime": "2017-12-12", "mind": "reconstitute"},
        ]
    }
