from __future__ import absolute_import

import sys

import click
from cateow import cateow as cateow_core
from cateow import utils


@click.command()
@click.option('--meanies', default=None,
              help='Path to a specific file with mean phrases')
@click.option('--kitty', default=None, help='Path to a specific kitty file')
@click.option('--meanie', default=None, help='What kitty will say')
def cli(meanie=None, kitty=None, meanies=None):
    # pylint: disable=no-member
    try:
        if meanie is None:
            meanie = cateow_core.get_meanie(meanies)
        kitty_template = cateow_core.get_kitty(kitty_file_path=kitty)
        kitty_cat = cateow_core.cateow(meanie, kitty_template)
    except utils.CateowException as ex:
        click.echo(ex.message)
        sys.exit(1)
    click.echo(kitty_cat)
    sys.exit(0)


if __name__ == '__main__':
    cli(sys.argv[1:])
