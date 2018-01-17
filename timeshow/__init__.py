from bottle import Bottle

from .config import CONFIG
from .views import app as sub_app


app = Bottle()

app.merge(sub_app)

app.config.load_dict(CONFIG)
