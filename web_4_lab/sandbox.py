from web_4_lab.service import get_all_clients, get_client
from web_4_lab.utils import get_app


def command():
    with get_app().app_context() as app:
        # print(get_all_clients())
        print(get_client(id_=1))


if __name__ == '__main__':
    command()
