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


if __name__ == "__main__":
    test_crypto()
    test_models()
