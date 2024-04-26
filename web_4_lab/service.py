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


# # Создать новый запрос
# def create_contact_req(json_data):
#     try:
#         # INSERT запрос в БД
#         db.session.execute(text(f"INSERT INTO clients "
#                                 f"(name, mail, phone_number, message) "
#                                 f"VALUES ("
#                                 f"'{json_data['name']}', "
#                                 f"'{json_data['mail']}', "
#                                 f"'{json_data['phone_number']}', "
#                                 f"'{json_data['message']}')"
#                                 ))
#         # Подтверждение изменений в БД
#         db.session.commit()
#         # Возвращаем результат
#         return {'message': "Client Created!"}
#         # если возникла ошибка запроса в БД
#     except Exception as e:
#         # откатываем изменения в БД
#         db.session.rollback()
#         # возвращаем dict с ключом 'error' и текcтом ошибки
#         return {'message': str(e)}
#

# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        get_db().session.execute(f"DELETE FROM clients WHERE id = {id}")
        get_db().session.commit()
        return {'message': "Client Deleted!"}
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}
