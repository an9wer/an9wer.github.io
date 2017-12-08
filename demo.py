from bottle import (
    Bottle, route, run, template, get, post, request, static_file)


@route("/")
def index():
    return static_file("time-show.html", root="./")

@route("/static/<path:path>")
def static(path):
    return static_file(path, root="./static/")

@route("/api/load/")
def load():
    return {
        "items": [
            {"datetime": "2017-11-26", "mind": "I'll get it" },
            {"datetime": "2017-11-30", "mind": "demo it."},
            {"datetime": "2017-12-03", "mind": "dame cool."},
            {"datetime": "2017-12-05", "mind": "scroll to bottom load more"},
            {"datetime": "2017-12-07", "mind": "css transition"},
            {"datetime": "2017-12-08", "mind": "ease loading"}
        ]
    }

if __name__ == "__main__":
    run(host="0.0.0.0", port="8080", debug=True)
