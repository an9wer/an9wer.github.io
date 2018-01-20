import datetime
import sqlite3

from bottle import cached_property
from .config import CONFIG
from .utils.crypto import Engima


_engima = Engima(CONFIG["app"]["secret_key"])


def adapt_encrypted_timestamp(dt):
    """
    :param dt: datetime.datetime object
    """
    return _engima.encrypt(dt.strftime("%Y-%m-%d %H:%M:%S.%f"))

def convert_encrypted_timestamp(ec_dt):
    """
    :param ec_dt: encrypted datetime which is bytes object

    Note: Converter functions always get called with a bytes object, no matter
    under which data type you sent the value to SQLite. So we need to decode
    it here.
    """
    return datetime.datetime.strptime(_engima.decrypt(ec_dt),
                                      "%Y-%m-%d %H:%M:%S.%f")

def adapt_encrypted_text(tt):
    """
    :param text: str object
    """
    return _engima.encrypt(tt)

def convert_encrypted_text(ec_tt):
    """
    :param ec_text: encrypted text which is bytes object
    """
    return _engima.decrypt(ec_tt)


class auto_commit:

    def __init__(self, func):
        self.func = func

    def __get__(self, ins, cls):
        def wrapper(*args, **kwargs):
            # print("before CRUD :", ins.con.in_transaction)      # for test
            res = self.func(ins, *args, **kwargs)
            # print("after CRUD  :", ins.con.in_transaction)      # for test
            ins.con.commit()
            # print("after commit:", ins.con.in_transaction)      # for test
            return res
        return wrapper


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
                                detect_types=self._db.PARSE_DECLTYPES)

    @cached_property
    def cur(self):
        return self.con.cursor()

    def register_adapter(self, type, adapter):
        return self._db.register_adapter(type, adapter)

    def register_converter(self, typename, converter):
        return self._db.register_converter(typename, converter)


class TimeShow(Sqlite):

    def __init__(self, name, encrypt=True):
        self.fields = "id", "created", "mind"
        self.name = name            # table name
        self.encrypt = encrypt      # whether to encrypt mind
        self.sql = []               # store sql history

        # if encrypt is True, encrypt sqlite TIMESTAMP/TEXT type value,
        # otherwise use sqlite default TIMESTAMP/TEXT type (in python
        # sqlite3 module, there is a default adapter and converter for
        # TIMESTAMP type.)
        if encrypt:
            # timestamp adapter/converter
            self.register_adapter(datetime.datetime, adapt_encrypted_timestamp)
            self.register_converter("timestamp", convert_encrypted_timestamp)
            # text adapter/converter
            self.register_adapter(str, adapt_encrypted_text)
            self.register_converter("text", convert_encrypted_text)

    @auto_commit
    def execute(self, sql, value=None):
        assert isinstance(value, (tuple, type(None)))
        self.sql.append(sql)
        if isinstance(value, tuple):
            self.cur.execute(sql, value)
        else:
            self.cur.execute(sql)

    def create_table(self):
        self.execute(
            "CREATE TABLE %s ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "created TIMESTAMP NOT NULL, "
                "mind TEXT NOT NULL)" % self.name
        )

    def drop_table(self):
        self.execute("drop table if exists %s" % self.name)

    def __setitem__(self, key, value):
        if not isinstance(value, tuple):
            raise ValueError("value must be tuple, "
                             "instead of (%r)" % type(value))

        if len(value) != 2:
            raise ValueError("value length have two items, "
                             "instead of (%d)" % len(value))

        if (not isinstance(value[0], datetime.datetime)
                and not isintance(value[1], str)):
            raise ValueError("value should be the type of (datetime, str)")

        if key == "new":
            self.execute(
                "insert into %s(created, mind) values(?, ?)" % (self.name), value
            )
        elif isinstance(key, int):
            self.execute(
                "update from %s set created = (?), mind = (?) "
                "where id = %d " % (self.name, key), value
            )
        else:
            raise KeyError("unknown key(%r)" % key)

    def __getitem__(self, key):
        if key == "all":
            self.execute("select * from %s" % self.name)
            return self.cur.fetchall()
        elif isinstance(key, int):
            self.execute("select * from %s where id = %d" % (self.name, key))
            return self.cur.fetchone()
        else:
            raise KeyError("unknown key(%r)" % key)

    def __delitem__(self, key):
        if isinstance(key, int):
            self.execute("delete from %s where id = %d" % (self.name, key))
        else:
            raise KeyError("unknown key(%r)" % key)
