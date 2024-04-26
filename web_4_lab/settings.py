import os
import pathlib

BASE_DIRPATH: str = str(pathlib.Path(__file__).parent.parent)

ENV_FILENAME: str = ".env"

ENV_FILEPATH: str = os.path.join(BASE_DIRPATH, ENV_FILENAME)

DB_URL = f'sqlite:///{os.path.join(BASE_DIRPATH, "db.sqlite")}'

TEMPLATES_DIRPATH: str = os.path.join(BASE_DIRPATH, "templates")

STATIC_DIRPATH: str = os.path.join(BASE_DIRPATH, "static")
