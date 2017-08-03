from __future__ import absolute_import

import re

from cateow import constants


class CateowException(Exception):
    pass


def split_text_in_lines(text):
    """Splits text in lines of a length specified in the constants file.

    Args:
        text (str): the text to be split in lines

    Returns:
        List of lines.
    """
    max_len_length = constants.MAX_LEN_LINE
    lines = []
    phrases = text.split('\n')
    phrases = [phrase for phrase in phrases if phrase != '']
    for phrase in phrases:
        current_phrase = phrase
        while len(current_phrase) > max_len_length:
            space_character_distance = 0
            if current_phrase[max_len_length - 1] != ' ':
                space_character_distance = get_last_space_index(
                    current_phrase[:max_len_length])
            space_character_index = max_len_length - space_character_distance
            lines.append(current_phrase[:space_character_index - 1])
            current_phrase = current_phrase[space_character_index:]
        lines.append(current_phrase)
    return lines


def make_balloon(text):
    """Creates a balloon of a length specified in the constants file, containing
    the text specified in the parameter. The balloon has top, bottom and
    margins.
    The top and the bottom are represented by lines (`-` and `_` for bottom)
    and the margin from `<`, `>` or `\`, `/` depending on the number of lines
    in the text.

    Args:
        text (str): the text the balloon will contain

    Example:

          ___________________________
        < Lorem ipsum dolor sit amet. >
          ---------------------------
         _______________________________________
        / Lorem ipsum dolor sit amet, consectetur \
        \ adipiscing elit.                        /
          ---------------------------------------

          ----------------------------------------
        / Lorem ipsum dolor sit amet, consectetur \
        | adipiscing elit. Sed sodales egestas    |
        | lectus, non porttitor metus cursus nec. |
        \ Suspendisse potenti.                    /
          ---------------------------------------


    Returns:
        A balloon containing the text specified.
    """
    lines = split_text_in_lines(text)
    len_longest_line = max([len(line) for line in lines])
    balloon = []
    balloon.append(constants.LINE_TEMPLATE.format(
        text="_" * len_longest_line, margin_left=' ', margin_right=' '))
    for line in lines:
        if lines.index(line) == 0:
            if len(lines) == 1:
                margin_left = '<'
                margin_right = '>'
            else:
                margin_left = '/'
                margin_right = '\\'
        elif lines.index(line) == len(lines) - 1:
            margin_left = '\\'
            margin_right = '/'
        else:
            margin_left = margin_right = '|'
        if len(line) < len_longest_line:
            line = "{line}{spaces}".format(
                line=line, spaces=" " * (len_longest_line - len(line)))
        balloon.append(constants.LINE_TEMPLATE.format(
            text=line, margin_left=margin_left, margin_right=margin_right))
    balloon.append(constants.LINE_TEMPLATE.format(
        text="-" * len_longest_line, margin_left=' ', margin_right=' '))
    return '\n'.join(balloon)


def escape_character(input_string, sequence, replace_with, ignore_first=3):
    """Some kitties might have some characters which need to be escaped.
    For instance, the characters `{` and `}`. This function replaces those
    characters with the escaped version of themselves.

    Args:
        input_string (str): string which contains characters which need to
            be escaped
        sequence (str): sequence which needs to be replaced
        replace_with (str): sequence which will replace `sequence`
        ignore_first (int, optional): represents the number of first characters
            which can be ignored. For example, a kitty has in its template the
            sequences `{balloon}` and `{way}` which represent the parameters
            used to format the template. Those need not to be escaped. Default
            value is 3.

    Returns:
        The `input_string` string with the `sequence` characters replaced with
        `replace_with` sequence, except for the first `ignore_first`
        appearences.
    """
    character_count = input_string.count(sequence)
    if character_count <= ignore_first:
        return input_string
    revert_string = input_string[::-1]
    revert_string = re.sub(sequence, replace_with,
                           revert_string,
                           count=character_count - ignore_first)
    return revert_string[::-1]


def get_last_space_index(input_string, start=None):
    """Finds the last space character in a substring of `input_string`
    starting from the `start` index.

    Args:
        input_string (str): string in which the space character will be
            searched
        start (int, optional): index showing where the substring starts.
        Default value is 0."""
    return input_string[start:][::-1].find(' ')
