import re

import constants


class CateowException(Exception):
    pass


def split_text_in_lines(text):
    max_len_length = constants.MAX_LEN_LINE
    lines = []
    phrases = text.split('\n')
    phrases = list(filter(lambda x: x != '', phrases))
    for phrase in phrases:
        current_phrase = phrase
        while len(current_phrase) > max_len_length:
            space_character_distance = 0
            if current_phrase[max_len_length] != ' ':
                space_character_distance = get_last_space_index(current_phrase)
            space_character_index = max_len_length - space_character_distance
            lines.append(current_phrase[:space_character_index])
            current_phrase = current_phrase[space_character_index + 1:]
        lines.append(current_phrase)
    return lines


def make_balloon(text):
    lines = split_text_in_lines(text, constants.MAX_LEN_LINE)
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
    character_count = input_string.count(sequence)
    if character_count <= ignore_first:
        return input_string
    revert_string = input_string[::-1]
    revert_string = re.sub(sequence, replace_with,
                           revert_string,
                           count=character_count - ignore_first)
    return revert_string[::-1]


def get_last_space_index(input_string, start=0):
    return input_string[start::-1].find(' ')
