def main():
    from web_4_lab.utils import get_app
    get_app()
    from web_4_lab.route import init_routes
    init_routes()
    get_app().run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
