from enum import Enum


class LABEL(Enum):
    start_end = 0
    scan = 1
    decision = 2
    print = 3
    process = 4
    arrow_line_up = 5
    arrow_line_down = 6
    arrow_line_right = 7
    arrow_line_left = 8
    pointer = 9


mermaid_delete_characters: () = (
    '(',
    ')',
    '[',
    ']',
    '>',
    '{',
    '}',
    '/',
    '\\'
)

block_open: {} = {
    'start_end': '([',
    'scan': '[/',
    'decision': '{{',
    'print': '[\\',
    'process': '['
}

block_close: {} = {
    'start_end': '])',
    'scan': '/]',
    'decision': '}}',
    'print': '/]',
    'process': ']'
}

supported_languages: [] = [
    'pseudo_language',
    'mermaid',
    'python'
]

