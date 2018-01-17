import datetime
import sqlite3

from .config import CONFIG
from .utils.crypto import Engima

engima = Engima(CONFIG["app"]["secret_key"])

def adapt_datetime(dt):
    """
    :param dt: datetime.datetime object
    """
    return engima.encrypt(dt.strftime("%Y-%m-%d %H:%M:%S.%f"))

def convert_datetime(ec_dt):
    """
    :param ec_dt: encrypted datetime which is bytes object

    Note: Converter functions always get called with a bytes object, no matter
    under which data type you sent the value to SQLite. So we need to decode
    it here.
    """
    return datetime.datetime.strptime(engima.decrypt(ec_dt),
                                      "%Y-%m-%d %H:%M:%S.%f")

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter("datetime", convert_datetime)


def adapt_text(tt):
    """
    :param text: str object
    """
    return engima.encrypt(tt)

def convert_text(ec_tt):
    """
    :param ec_text: encrypted text which is bytes object
    """
    return engima.decrypt(ec_tt)

sqlite3.register_adapter(str, adapt_text)
sqlite3.register_converter("text", convert_text)

#con = sqlite3.connect("timeshow.db", detect_types=sqlite3.PARSE_DECLTYPES)
#cur = con.cursor()

