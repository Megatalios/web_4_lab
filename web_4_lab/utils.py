from functools import lru_cache

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from web_4_lab.settings import DB_URL, TEMPLATES_DIRPATH, STATIC_DIRPATH

_app = Flask(
    __name__,
    template_folder=TEMPLATES_DIRPATH,
    static_folder=STATIC_DIRPATH,
    static_url_path="/static"
)
_app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL


def get_app():
    return _app


_db = SQLAlchemy(get_app())


def get_db() -> SQLAlchemy:
    return _db


def drop_database():
    get_db().drop_all()


def create_tables():
    get_db().session.execute(text(
        "create table clients if not exists ("
        "id integer PRIMARY KEY autoincrement",
        "name varchar(255) NOT NULL",
        "email varchar(255)NOT NULL",
        "phone_number varchar(25)NOT NULL",
        "message varchar(255)"
    ))
