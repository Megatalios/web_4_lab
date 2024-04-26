from web_4_lab.service import create_client
from web_4_lab.utils import get_app


def command():
    with get_app().app_context() as app:
        # print(get_all_clients())
        # print(get_client(id_=1))
        # create_client(
        #     name="asfasf",
        #     mail="asf",
        #     phone_number="asf",
        #     message="asf"
        # )
        client = create_client(
            name="Arsen",
            mail="arpa2",
            phone_number="asfasf",
            message="Asf"
        )
        print(client)


if __name__ == '__main__':
    command()
