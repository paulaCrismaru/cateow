MAX_LEN_LINE = 39
LINE_TEMPLATE = "{margin_left} {text} {margin_right}"


def split_text_in_lines(text, max_len_length):
    lines = []
    line = ""
    for word in text.split():
        if len(line) + len(word) + 1 <= max_len_length:
            if line == '':
                line = word
            else:
                line = ' '.join([line, word])
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def make_balloon(text):
    lines = split_text_in_lines(text, MAX_LEN_LINE)
    len_longest_line = max([len(line) for line in lines])
    balloon = []
    balloon.append(LINE_TEMPLATE.format(
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
        balloon.append(LINE_TEMPLATE.format(
            text=line, margin_left=margin_left, margin_right=margin_right))
    balloon.append(LINE_TEMPLATE.format(
        text="-" * len_longest_line, margin_left=' ', margin_right=' '))
    return '\n'.join(balloon)
