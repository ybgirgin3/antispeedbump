from pathlib import Path
from pprint import pprint

import click

from antispeedbump.bot import Bot


@click.group()
def cli():
    pass


@cli.command()
@click.option("--username", type=str, default="", help="username to dig profile in")
@click.option(
    "--collect", is_flag=True, default=False, help="Download last post or not"
)
def find(username: str, collect: bool):
    if not Path("database.db").exists():
        from antispeedbump.commons import SQL_ALCHEMY_ENGINES, _create_table

        _create_table("Sites", SQL_ALCHEMY_ENGINES["antispeedbump"])
        _create_table("Queue", SQL_ALCHEMY_ENGINES["antispeedbump"])

    ret = Bot(
        target_user=username,
        will_create_content=collect,
    ).get_data_from_another()
    # print(ret['full_name'], ret['profile_picture'])
    pret = {"full_name": ret["full_name"],
            "profile_picture": ret["profile_picture"]}
    pprint(pret)


@cli.command()
@click.option("--type", type=str, default="post", help="standart post")
def post(type: str):
    import json

    # read creds
    with open('credientials.json') as f:
        creds = json.loads(f.read())

    ret = Bot(
        username=creds['username'],
        password=creds['password'],

        # username="bekocankod",
        # password=")d3::b%&.X,u3^J",
        post_type=type).post_content()
    pprint(ret)


if __name__ == "__main__":
    cli()
