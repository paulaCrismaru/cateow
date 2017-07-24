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
    for character, replacement in utils.ESCAPE_CHARACTERS:
        kitty = utils.escape_character(kitty, character, replacement)
    try:
        return str(kitty).format(balloon=balloon, way="\\")
    except (KeyError, ValueError):
        return "Kitty formating failed :("


@click.command()
@click.option('--kitty', default=None, help='Path to a specific kitty file')
@click.option('--meanie', default=None, help='What kitty will say')
def cli(meanie, kitty):
    file_path = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))

    if meanie is None:
        meanies_path = os.sep.join([file_path, MEANIES_FILE_PATH])
        meanie = random.choice(open(meanies_path).readlines())

    if kitty is None:
        path = os.sep.join([file_path, KITTIES_PATH])
        if os.path.isdir(path):
            kitty_file_name = random.choice(os.listdir(path))
            kitty_file_path = os.sep.join([path, kitty_file_name])
    else:
        kitty_file_path = kitty
        if not os.path.isabs(kitty):
            kitty_file_path = os.sep.join([os.curdir, kitty])
        if not os.path.isfile(kitty_file_path):
            print("No such file: '{}'".format(kitty_file_path))

    with open(kitty_file_path, 'r') as kitty_file:
        kitty = kitty_file.read()
    print(cateow(meanie, kitty))
