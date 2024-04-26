from flask import make_response, render_template, request

from arpakitlib.safely_transfer_to_json import safely_transfer_to_json_str
from web_4_lab.service import get_all_clients, get_client, get_client_by_name, remove_client_by_id, create_client
from web_4_lab.utils import get_app


@get_app().get("/all_clients")
def route_all_clients():
    return safely_transfer_to_json_str({"clients": get_all_clients()})


@get_app().get("/")
@get_app().get("/index")
def route_index():
    return render_template("index.html")


@get_app().getget("/about")
def route_about():
    return render_template("about_us.html")


@get_app().get('/contacts')
def route_contacts():
    return render_template("contacts.html")


@get_app().get('/success')
def route_success():
    return render_template("success.html")


@get_app().get('/feedback')
def route_feedback():
    return render_template("feedback.html")


@get_app().get('/api/contactrequest/<int:id>', methods=['GET'])
# Получаем запись по id
def route_get_contact_req_by_id(id: int):
    return safely_transfer_to_json_str(get_client(id))


@get_app().get('/api/contactrequest/author/<string:name>', methods=['GET'])
# Получаем запись по имени пользователя
def route_get_client_by_name(name: str):
    name = name.strip()
    if not name:
        return make_response(safely_transfer_to_json_str({"error": "Bad request"}), 400)
    else:
        return make_response(safely_transfer_to_json_str(get_client_by_name(name=name)), 200)


@get_app().post('/api/contactrequest')
# Обработка запроса на создание новой записи в БД
def route_create_client():
    if (
            not request.json
            or "name" not in request.json
            or "mail" not in request.json
            or "phone_number" not in request.json
            or "message" not in request.json
    ):
        return make_response(safely_transfer_to_json_str({"error": "Not found"}), 404)

    client_data = create_client(
        name=request.json["name"],
        mail=request.json["mail"],
        phone_number=request.json["phone_number"],
        message=request.json["message"]
    )
    return make_response(safely_transfer_to_json_str(client_data), 200)


@get_app().delete("/api/contactrequest/<int:id>")
def route_delete_contact_req_by_id(id: int):
    remove_client_by_id(id)
    return make_response(safely_transfer_to_json_str({'message': "Client was removed"}), 400)


@get_app().get("/notfound")
def route_not_found():
    return render_template('404.html', title='404', err={'error': 'Not found', 'code': 404})


def init_routes():
    pass
