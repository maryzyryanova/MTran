TOKEN_PATTERN = r'([a-zA-z]+\[\]|;|\d+\.\d+|\w+|\"\w*\"|\(|\)|\{|\}|\[|\]|\+=+|-=+|\*=+|/=+|%=+|\++|-+|\*+|\/+|%+|!=+|<+|<=+|>+|>=+|=+|;|.)|(.+)"'

FLOAT_PATTERN = r'^\d+|\d+\.\d+$'
INT_PATTERN = r'^\d+$'
STRING_PATTERN = r'^"[a-zA-Z]*"$'
IDENTIFIER_PATTERN = r'^[a-zA-Z]\w*$'
IDENTIFIER_DESC = 'Identifier of type'

keywords = {
    'break': 'Flow control keyword',
    'continue': 'Flow control keyword',
    'while': 'Flow control keyword',
    'for': 'Flow control keyword',
    'if': 'Flow control keyword',
    'else': 'Flow control keyword',
    'return': 'Flow control keyword',
    '(': 'Parenthesis',
    ')': 'Parenthesis',
    '{': 'Parenthesis',
    '}': 'Parenthesis',
    '[': 'Parenthesis',
    ']': 'Parenthesis',
    ',': 'Comma separator',
    ';': 'End of instruction'
}

operators = {
    '+': 'Arithmetic operator',
    '-': 'Arithmetic operator',
    '*': 'Arithmetic operator',
    '/': 'Arithmetic operator',
    '%': 'Arithmetic operator',
    '++': 'Arithmetic operator',
    '--': 'Arithmetic operator',
    '+=': 'Arithmetic operator',
    '-=': 'Arithmetic operator',
    '*=': 'Arithmetic operator',
    '/=': 'Arithmetic operator',
    '%=': 'Arithmetic operator',
    '=': 'Assignment operator',
    'print': 'STD function',
    'pow': 'STD function',
    'sqrt': 'STD function',
    'read': 'STD function',
    'readint': 'STD function',
    'readfloat': 'STD function',
    '==': 'Comparison operator',
    '!=': 'Comparison operator',
    '<': 'Comparison operator',
    '>': 'Comparison operator',
    '<=': 'Comparison operator',
    '>=': 'Comparison operator'
}

data_types = {
    'string': 'Data type',
    'float': 'Data type',
    'int': 'Data type',
    'string[]': 'Data type',
    'float[]': 'Data type',
    'float[]': 'Data type'
}
