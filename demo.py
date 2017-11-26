from bottle import (
    Bottle, route, run, template, get, post, request, static_file)


@route("/")
def index():
    return static_file("time-show.html", root="./")

@route("/static/<path:path>")
def static(path):
    return static_file(path, root="./static/")

if __name__ == "__main__":
    run(host="0.0.0.0", port="8080", debug=True)
