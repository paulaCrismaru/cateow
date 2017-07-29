import os

MAX_LEN_LINE = 39
LINE_TEMPLATE = "{margin_left} {text} {margin_right}"
ESCAPE_CHARACTERS = [
    ('{', '{{'),
    ('}', '}}')
]
KITTIES_PATH = 'kitties'
MEANIES_FILE_PATH = os.sep.join(['meanies', 'meanies.mean'])
