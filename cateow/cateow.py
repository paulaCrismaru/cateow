from __future__ import print_function

import click
import inspect
import os
import random


from . import utils

KITTIES_PATH = 'kitties'
MEANIES_FILE_PATH = os.sep.join(['meanies', 'meanies.mean'])


def cateow(text, kitty):
    balloon = utils.make_balloon(text)
    try:
        return str(kitty).format(balloon=balloon, way="\\")
    except (KeyError, ValueError):
        return "Kitty formating failed :("


@click.command()
@click.option('--meanie', default=None, help='What kitty will say')
def cli(meanie):
    file_path = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.sep.join([file_path, KITTIES_PATH])
    if meanie is None:
        meanies_path = os.sep.join([file_path, MEANIES_FILE_PATH])
        meanie = random.choice(open(meanies_path).readlines())
    if os.path.isdir(path):
        kitty_file_name = random.choice(os.listdir(path))
        with open(os.sep.join([path, kitty_file_name]), 'r') as kitty_file:
            kitty = kitty_file.read()
        print(cateow(meanie, kitty))
