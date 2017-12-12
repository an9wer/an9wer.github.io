from bottle import Bottle

from .views import app as sub_app

app = Bottle()

app.merge(sub_app)
