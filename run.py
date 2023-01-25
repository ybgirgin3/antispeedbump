from pprint import pprint

import click

from bot import Bot


@click.group()
def cli():
    pass


@cli.command()
@click.option('--username', type=str, default="", help="username to dig profile in")
@click.option('--collect', is_flag=True, default=False, help="Download last post or not")
@click.option('--post_index', type=int, default=0, help="post_index of content")
@click.option('--shortcode', type=str, default="", help="shortcode of content")
def find(username: str, collect: bool, post_index: int, shortcode: str):
    ret = Bot(target_user=username,
              will_create_content=collect,
              post_index=post_index,
              shortcode=shortcode
              ).get_data_from_another()
    print(ret['full_name'], ret['profile_picture'])


@cli.command()
@click.option('--type', type=str, default="post", help="standart post")
def post(type: str):
    ret = Bot(post_type=type).post_content()
    pprint(ret)


if __name__ == '__main__':
    cli()
