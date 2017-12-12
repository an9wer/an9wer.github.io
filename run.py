from bottle import run

from timeshow import app


if __name__ == "__main__":
    run(app, host="0.0.0.0", port="8080", debug=True, reloader=True)
