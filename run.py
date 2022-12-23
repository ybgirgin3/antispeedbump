import click
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
@click.option('--path', type=str, default=False)
@click.option('--description', type=str, default=False)
def post(path: str, description: str):
    image = {
            "path":  path,
            "description": description
            }
    ret = Bot(image=image).post_content()
    print(ret)




if __name__ == '__main__':
    cli()

