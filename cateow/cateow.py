from __future__ import print_function

import os
import random


import constants
import utils


def cateow(text, kitty_template):
    balloon = utils.make_balloon(text)
    kitty_template = escape_kitty_template(kitty_template)
    try:
        return str(kitty_template).format(balloon=balloon, way="\\")
    except (KeyError, ValueError):
        raise utils.CateowException(
            "Kitty formating failed :(")


def get_meanie(meanies_path):
    if meanies_path is None:
        meanies_path = os.sep.join([os.path.dirname(__file__),
                                    constants.MEANIES_FILE_PATH])
    else:
        if not os.path.isabs(meanies_path):
            meanies_path = os.sep.join([os.getcwd(), meanies_path])
        if not os.path.isfile(meanies_path):
            raise utils.CateowException(
                "No such file: '{}'".format(meanies_path))
    with open(meanies_path) as meanies_file:
        meanie = random.choice(meanies_file.readlines())
    return meanie


def get_kitty(kitty_file_path):
    if kitty_file_path is None:
        path = os.sep.join([os.path.dirname(__file__), constants.KITTIES_PATH])
        if os.path.isdir(path):
            kitty_file_name = random.choice(os.listdir(path))
            kitty_file_path = os.sep.join([path, kitty_file_name])
    else:
        if not os.path.isabs(kitty_file_path):
            kitty_file_path = os.sep.join([os.getcwd(), kitty_file_path])
    if not os.path.isfile(kitty_file_path):
        raise utils.CateowException(
            "No such file: '{}'".format(kitty_file_path))

    with open(kitty_file_path, 'r') as kitty_file:
        kitty = kitty_file.read()
    return kitty


def escape_kitty_template(kitty_template):
    for character, replacement in constants.ESCAPE_CHARACTERS:
        kitty_template = utils.escape_character(
            kitty_template, character, replacement)
    return kitty_template
