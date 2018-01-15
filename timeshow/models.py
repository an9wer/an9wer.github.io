import datetime
import sqlite3

from .utils.crypto import Engima

engima = Engima()

con = sqlite3.connect("timeshow.db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

def adapt_datetime(dt):
    """
    :param dt: datetime.datetime object
    """
    return engima.encrypt(dt.strftime("%Y-%m-%d %H:%M:%S.%f"))

def convert_datetime(ec_dt):
    """
    :param ec_dt: encrypted datetime bytes

    Note: Converter functions always get called with a bytes object, no matter
    under which data type you sent the value to SQLite. So we need to decode
    it here.
    """
    bt_dt = engima.decrypt(ec_dt)   # by_dt is decrypted datetime bytes
    return datetime.datetime.strptime(str(bt_dt, "utf-8"),
                                      "%Y-%m-%d %H:%M:%S.%f")

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter("datetime", convert_datetime)
