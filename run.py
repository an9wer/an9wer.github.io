from bottle import run


if __name__ == "__main__":
    run('timeshow:app', host="0.0.0.0", port="8080", debug=True, reloader=True)
