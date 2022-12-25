from utils import FileProcess
from pprint import pprint
from bot import Bot
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', type=str, default="", help="username to dig profile in")
@click.option('--create', type=bool, default=False, help="Download last post or not")
def find(username: str, create: bool):
    ret = Bot(
        target_user=username, will_create_content=create
    ).get_data_from_another()
    pprint(ret)


@cli.command()
def post():
    ret = Bot().post_content()
    print(ret)


if __name__ == '__main__':
    cli()
