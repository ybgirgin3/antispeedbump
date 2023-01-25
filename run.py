from pprint import pprint
from pathlib import Path
import os

import click

from bot import Bot





@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', type=str, default="", help="username to dig profile in")
@click.option('--collect', is_flag=True, default=False, help="Download last post or not")
def find(username: str, collect: bool):
    if not Path("antispeedbump.db").exists():
        from commons import SQL_ALCHEMY_ENGINES, _create_table
        _create_table("Sites", SQL_ALCHEMY_ENGINES['sites'])


    ret = Bot(target_user=username,
              will_create_content=collect,
              ).get_data_from_another()
    print(ret['full_name'], ret['profile_picture'])


@cli.command()
@click.option('--type', type=str, default="post", help="standart post")
def post(type: str):
    ret = Bot(post_type=type).post_content()
    pprint(ret)


if __name__ == '__main__':
    cli()
