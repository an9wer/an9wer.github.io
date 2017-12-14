import datetime
import sqlite3


con = sqlite3.connect("timeshow.db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

def adapt_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S.%f")

def convert_datetime(byte_dt):
    # Converter functions always get called with a bytes object,
    # no matter under which data type you sent the value to SQLite.
    # So we need to decode it here.
    return datetime.datetime.strptime(byte_dt.decode(), "%Y-%m-%d %H:%M:%S.%f")

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter("datetime", convert_datetime)
