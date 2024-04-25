from sqlalchemy import text
from labapp import db # type: ignore
from flask_sqlalchemy import SQLAlchemy

"""
    В данном модуле реализуются CRUD-методы для работы с БД
"""

def get_all_clients():
    result = []     # создаем пустой список
    # Получаем итерируемый объект, где содержатся все строки таблицы contactrequests
    rows = db.session.execute(text("SELECT * FROM clients")).fetchall()
    # Каждую строку конвертируем в стандартный dict, который Flask может трансформировать в json-строку
    for row in rows:
        result.append(dict(row))
    # возвращаем dict, где result - это список с dict-объектов с информацией
    return {'clients': result}


def test():
    try:
        result = db.session.execute(text("SELECT 1"))
        if result.fetchone():
            return "База данных подключена корректно!"
        else:
            return "Ошибка подключения к базе данных"
    except Exception as e:
        return f"Ошибка: {e}"

# Получаем запрос с фильтром по id
def get_contact_req_by_id(id):
    result = db.session.execute(f"SELECT * FROM clients WHERE id = {id}").fetchone()
    return dict(result)


# Получаем все запросы по имени автора
def get_contact_req_by_author(name):
    result = []
    rows = db.session.execute(f"SELECT * FROM clients WHERE firstname = '{name}'").fetchall()
    for row in rows:
        result.append(dict(row))
    return {'clients': result}


# Создать новый запрос
def create_contact_req(json_data):
    try:
        # INSERT запрос в БД
        db.session.execute(text(f"INSERT INTO clients "
                           f"(name, mail, phone_number, message) "
                           f"VALUES ("
                           f"'{json_data['name']}', "
                           f"'{json_data['mail']}', "
                           f"'{json_data['phone_number']}', "
                           f"'{json_data['message']}')"
                           ))
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return {'message': "Client Created!"}
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и текcтом ошибки
        return {'message': str(e)}


# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.execute(f"DELETE FROM clients WHERE id = {id}")
        db.session.commit()
        return {'message': "Client Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

