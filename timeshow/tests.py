""" unit testing
"""


def test_crypto():
    from .utils.crypto import Engima
    engima = Engima("passwd")
    text = "some text"
    ciphertext = engima.encrypt(text)
    assert isinstance(ciphertext, bytes)
    plaintext = engima.decrypt(ciphertext)
    assert isinstance(plaintext, str)
    assert plaintext == text


def test_models():
    import datetime
    from .models import sqlite3
    con = sqlite3.connect("timeshow.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    values = (datetime.datetime.now(), "whatever")
    cur.execute("delete from timeshow")
    cur.execute("insert into timeshow(created, mind) values(?, ?)", values)
    con.commit()
    cur.execute("select created, mind from timeshow")
    assert cur.fetchone() == values
    con.close()


if __name__ == "__main__":
    test_crypto()
    test_models()
