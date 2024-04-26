from flask import Response, jsonify, make_response, render_template

from arpakitlib.safely_transfer_to_json import safely_transfer_to_json_str
from web_4_lab.service import get_all_clients, get_client, get_client_by_name, remove_client_by_id
from web_4_lab.utils import get_app


@get_app().route("/all_clients")
def route_all_clients():
    return safely_transfer_to_json_str({"clients": get_all_clients()})


@get_app().route("/")
@get_app().route("/index")
def route_index():
    return render_template("index.html")


@get_app().route("/about")
def route_about():
    return render_template("about_us.html")


@get_app().route('/contacts')
def route_contacts():
    return render_template("contacts.html")


@get_app().route('/success')
def route_success():
    return render_template("success.html")


@get_app().route('/feedback')
def route_feedback():
    return render_template("feedback.html")


@get_app().route('/api/contactrequest/<int:id>', methods=['GET'])
# Получаем запись по id
def route_get_contact_req_by_id(id: int):
    return safely_transfer_to_json_str(get_client(id))


@get_app().route('/api/contactrequest/author/<string:name>', methods=['GET'])
# Получаем запись по имени пользователя
def route_get_client_by_name(name: str):
    name = name.strip()
    if not name:
        return make_response(safely_transfer_to_json_str({"error": "Bad request"}), 400)
    else:
        return make_response(safely_transfer_to_json_str(get_client_by_name(name=name)), 200)


# @app.route('/api/contactrequest', methods=['POST'])
# # Обработка запроса на создание новой записи в БД
# def create_contact_req():
#     # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
#     # или в данных нет обязательного поля 'firstname' или 'reqtext'
#     if not request.json or not 'name' in request.json:
#         # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
#         return bad_request()
#     # Иначе добавляем запись в БД отправляем json-ответ
#     else:
#         response = service.create_contact_req(request.json)
#         return json_response(response)
#
#
@get_app().route('/api/contactrequest/<int:id>', methods=['DELETE'])
def delete_contact_req_by_id(id: int):
    remove_client_by_id(id=id)
    return make_response(safely_transfer_to_json_str({'message': "Client was removed"}), 400)


@get_app().route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404})


def init_routes():
    pass
