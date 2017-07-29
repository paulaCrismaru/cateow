from __future__ import print_function

import os
import random

from cateow import constants
from cateow import utils


def cateow(text, kitty_template):
    """Creates a kitty using the `kitty_template` with the specified `text`
    wrapped in a balloon

    Args:
        text (str): the text the balloon will contain
        kitty_template (str): a template for the kitty which will be returned

    Returns:
        The kitty template formated with a balloon containig the specified text

    Raises:
        CateowException if the formating fails
    """

    balloon = utils.make_balloon(text)
    kitty_template = escape_kitty_template(kitty_template)
    try:
        return str(kitty_template).format(balloon=balloon, way="\\")
    except (KeyError, ValueError):
        raise utils.CateowException(
            "Kitty formating failed :(")


def get_meanie(meanies_path):
    """Returns a random meanie from the file located at `meanies_path`, if it's
    specified. Otherwise it will retrieve on from the default path.

    Args:
        meanies_path (str): represents a path to a file containig on each line
            a phrase which can be randomly chosen to be desplayed in the kitty
            ballloon

    Returns:
        A random string from the file located at `meanies_path`

    Raises:
        CateowException if the `meanies_path` is invalid
    """
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
    """Returns the kitty template from the specified file located at
    `kitty_file_path` or a random one from the default folder containing
    kitties.

    Args:
        kitty_file_path (str): path to file containing a kitty template

    Returns:
        The kitty template, with the special characters escaped, found at the
        specified file path

    Raises:
        CateowException if the `kitty_file_path` is invalid
    """
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
    """Escapes the special characters found int the constants file that might be
    found in the specified `kitty_template`

    Args:
        kitty_template (str): string containing the kitty template

    Returns:
        The kitty template with the special characters escaped"""
    for character, replacement in constants.ESCAPE_CHARACTERS:
        kitty_template = utils.escape_character(
            kitty_template, character, replacement)
    return kitty_template
