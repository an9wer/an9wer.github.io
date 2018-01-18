import datetime
import sqlite3

from bottle import cached_property
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

class Sqlite:

    @property
    def _db(self):
        return sqlite3

    @property
    def _db_name(self):
        return CONFIG["db"]["name"]

    @cached_property
    def con(self):
        return self._db.connect(self._db_name,
                                detect_types=self._db.PARSE_DECLTYPES,
                                isolation_level=None)

    @cached_property
    def cur(self):
        return self.con.cursor()

    def register_adapter(self, type, adapter):
        return self._db.register_adapter(type, adapter)

    def register_converter(self, typename, converter):
        return self._db.register_adapter(typename, converter)

    def auto_commit(self, func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            self.cur.commit()
            return res
        return wrapper


class TimeShow(Sqlite):

    def __init__(self, name, crypto=True):
        self.name = name
        self.crypto = crypto
        self.sql = ""
        self.fields = "id", "created", "mind"
        # datetime adapter/converter
        self.register_adapter(datetime.datetime, adapt_datetime)
        self.register_converter("datetime", convert_datetime)
        """
        # text adapter/converter
        self.register_adapter(str, adapt_text)
        self.register_converter("text", convert_text)
        """

    @cached_property
    def _engima(self):
        return Engima(CONFIG["app"]["secret_key"])

    def create_table(self):
        with self.con:
            self.sql = (
                """CREATE TABLE %s (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       created DATETIME NOT NULL,
                       mind TEXT NOT NULL)""" % self.name
            )
            self.cur.execute(self.sql)

    def drop_table(self):
        with self.con:
            self.sql = "drop table if exists %s" % self.name
            self.cur.execute(self.sql)

    def __setitem__(self, key, value):
        if not isinstance(value, tuple):
            raise ValueError("value must be tuple, "
                             "instead of (%r)" % type(value))

        if len(value) != 2:
            raise ValueError("value length have two items, "
                             "instead of (%d)" % len(value))

        if (not isinstance(value[0], datetime.datetime)
                and not isintance(value[1], str)):
            raise ValueError("value items should be (datetime, str)")

        if self.crypto:
            value = (value[0], self._engima.encrypt(value[1]))

        if key == "new":
            with self.con:
                self.sql = (
                    "insert into %s(created, mind) values(?, ?)" % self.name
                )
                self.cur.execute(self.sql, value)
        elif isinstance(key, int):
            with self.con:
                self.sql = (
                    "update from %s set created = (?), mind = (?) "
                    "where id = %d " % (self.name, key)
                )
                self.cur.execute(self.sql, value)
        else:
            raise KeyError("unknown key(%r)" % key)

    def __getitem__(self, key):
        if key == "all":
            with self.con:
                self.sql = "select * from %s" % self.name
                self.cur.execute(self.sql)
            return self.cur.fetchall()
        elif isinstance(key, int):
            with self.con:
                self.sql = "select * from %s where id = %d" % (self.name, key)
                self.cur.execute(self.sql)
            return self.cur.fetchone()
        else:
            raise KeyError("unknown key(%r)" % key)

    def __delitem__(self, key):
        if isinstance(key, int):
            with self.con:
                self.sql = "delete from %s where id = %d" % (self.name, key)
                self.cur.execute(self.sql)
        else:
            raise KeyError("unknown key(%r)" % key)
