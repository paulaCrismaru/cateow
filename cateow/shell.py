from __future__ import absolute_import

import sys

import click
from cateow import cateow as cateow_core
from cateow import utils


@click.command()
@click.argument('meanie_opt', nargs=-1, type=click.UNPROCESSED)
@click.option('--thinks', is_flag=True, help='Kitty thaughts of something')
@click.option('--meanies', default=None,
              help='Path to a specific file with mean phrases')
@click.option('--kitty', default=None, help='Path to a specific kitty file')
@click.option('--meanie', default=None, help='DEPRECATED! What kitty will say')
def cli(meanie, kitty, meanies, meanie_opt, thinks):
    # pylint: disable=no-member
    try:
        if meanie_opt:
            meanie = meanie_opt[0]
        elif not sys.stdin.isatty():
            line_args = [s.replace('\t', ' ' * 4) for s in sys.stdin]
            meanie = ''.join(line_args)
        elif meanie is None:
            meanie = cateow_core.get_meanie(meanies)
        if thinks:
            way = "o"
        else:
            way = "\\"
        kitty_template = cateow_core.get_kitty(kitty_file_path=kitty)
        kitty_cat = cateow_core.cateow(meanie, kitty_template, way)
    except utils.CateowException as ex:
        click.echo(ex.message)
        sys.exit(1)
    click.echo(kitty_cat)
    sys.exit(0)
