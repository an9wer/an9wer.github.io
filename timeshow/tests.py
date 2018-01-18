""" unit testing
"""

from .config import CONFIG


def test_crypto():
    from .utils.crypto import Engima
    engima = Engima(CONFIG["app"]["secret_key"])
    text = "some text"
    ciphertext = engima.encrypt(text)
    assert isinstance(ciphertext, bytes)
    plaintext = engima.decrypt(ciphertext)
    assert isinstance(plaintext, str)
    assert plaintext == text


def test_models():
    import datetime
    from .models import sqlite3
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute(
        """CREATE table timeshow (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             created DATETIME NOT NULL,
             mind TEXT NOT NULL)"""
    )
    values = (datetime.datetime.now(), "some minds")
    cur.execute("insert into timeshow(created, mind) values(?, ?)", values)
    cur.execute("select created, mind from timeshow")
    assert cur.fetchone() == values
    con.close()


def test_new_models():
    import datetime
    from .models import TimeShow
    ts = TimeShow("timeshow")
    ts.drop_table()
    ts.create_table()
    value1 = (datetime.datetime.now(), "some minds")
    value2 = (datetime.datetime.now(), "some other minds")
    ts["new"] = value1
    ts["new"] = value2
    assert [value[1:] for value in ts["all"]] == [value1, value2]
    del ts[1]
    assert [value[1:] for value in ts["all"]] == [value2]


if __name__ == "__main__":
    #test_crypto()
    #test_models()
    test_new_models()
