from sqlalchemy import text

from web_4_lab.utils import get_db


def get_all_clients():
    return get_db().session.execute(text("SELECT * FROM clients")).mappings().all()


# Получаем запрос с фильтром по id
def get_client(id_: int):
    return get_db().session.execute(text(f"SELECT * FROM clients WHERE id = {id_}")).mappings().one_or_none()


# # Получаем все запросы по имени автора
def get_client_by_name(name: str):
    result = []
    rows = get_db().session.execute(f"SELECT * FROM clients WHERE name = '{name}'")
    for row in rows:
        result.append(dict(row))
    return {'clients': result}


def create_client(name: str, mail: str, phone_number: str, message: str):
    get_db().session.execute(text(
        f"INSERT INTO clients "
        f"(name, mail, phone_number, message) "
        f"VALUES ("
        f"'{name}', "
        f"'{mail}', "
        f"'{phone_number}', "
        f"'{message}'"
        f")"
    ))
    get_db().session.commit()
    client_id = get_db().session.execute(text("SELECT last_insert_rowid()")).scalar()
    return dict(get_client(id_=client_id))


def remove_client_by_id(id_: int):
    get_db().session.execute(f"DELETE FROM clients WHERE id = {id_}")
    get_db().session.commit()
