import os
import getpass


def _get_secret_key():
    try: return os.environ["TIMESHOW_SECRET_KEY"]
    except KeyError: return getpass.getpass("Enter secret key: ")


CONFIG = {
    "db": {
        "engine": "sqlite3",
        "name": "timeshow.db",
    },
    "app": {
        "base_dir": os.path.dirname(__file__),
        "secret_key": _get_secret_key(),
    }
}
