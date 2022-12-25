import click
from utils import FileProcess
from bot import Bot


@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', type=str, default="", help="username to dig profile in")
def find(username: str):
    ret = Bot(target_user=username).get_data_from_another()
    print(ret)


@cli.command()
def post():
    ret = Bot().post_content()
    print(ret)


if __name__ == '__main__':
    cli()
