DROP TABLE IF EXISTS timeshow;

CREATE TABLE timeshow (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created datetime NOT NULL,
    mind TEXT NOT NULL
);
