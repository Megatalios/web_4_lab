# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app # type: ignore
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json
from . import dbservice    # подключение модуля с CRUD-методами для работы с БД из локального пакета


"""
    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения
"""


# Здесь маршруты и их обработчики
@app.route('/all_clients')
def get_all_clients():
    response = dbservice.get_all_clients()
    return json_response(response)


@app.route("/test")
def test():
    return dbservice.test()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about_us.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


"""

    Реализация обработчиков маршрутов (@app.route) REST API для модели ContactRequest (см. models.py).
    Обработчики маршрутов вызывают соответствующие HTTP-методам CRUD-операции из контроллера (см. dbservice.py)

"""


@app.route('/api/contactrequest', methods=['GET'])
# Получаем все записи contactrequests из БД
def get_contact_req_all():
    response = dbservice.get_contact_req_all()
    return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['GET'])
# Получаем запись по id
def get_contact_req_by_id(id):
    response = dbservice.get_contact_req_by_id(id)
    return json_response(response)


@app.route('/api/contactrequest/author/<string:firstname>', methods=['GET'])
# Получаем запись по имени пользователя
def get_get_contact_req_by_author(name):
    if not name:
        # то возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
        # Иначе отправляем json-ответ
    else:
        response = dbservice.get_contact_req_by_author(name)
    return json_response(response)


@app.route('/api/contactrequest', methods=['POST'])
# Обработка запроса на создание новой записи в БД
def create_contact_req():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в данных нет обязательного поля 'firstname' или 'reqtext'
    if not request.json or not 'name' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе добавляем запись в БД отправляем json-ответ
    else:
        response = dbservice.create_contact_req(request.json)
        return json_response(response)


@app.route('/api/contactrequest/<int:id>', methods=['DELETE'])
# Обработка запроса на удаление записи в БД по id
def delete_contact_req_by_id(id):
    response = dbservice.delete_contact_req_by_id(id)
    return json_response(response)


"""
    Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""


# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })


# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))


# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)
