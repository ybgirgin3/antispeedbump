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
@click.option('--post_index', type=int, default=0, help="post_index of content")

def find(username: str, create: bool, post_index: int):
    ret = Bot(
        target_user=username, will_create_content=create, post_index=post_index
    ).get_data_from_another()
    pprint(ret)


@cli.command()
def post():
    ret = Bot().post_content()
    print(ret)


if __name__ == '__main__':
    cli()
