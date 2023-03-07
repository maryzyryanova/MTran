import re, prettytable, patterns
from patterns import (
    TOKEN_PATTERN,
    IDENTIFIER_PATTERN,
    IDENTIFIER_DESC,
    INT_PATTERN,
    FLOAT_PATTERN,
    STRING_PATTERN
)
from errors import(
    LexicalError,
    SyntaxError
)
from parsing import Parser

class Analyzer(object):
    def __init__(self, source) -> None:
        self.lines = source.split('\n')
        self.identifiers = {}
        self.errors = False
        self.functions = {
            'read': 'string', 
            'readint': 'int',
            'readfloat': 'float',
            'sqrt': 'float',
            'pow': 'int'
        }
    
    def get_tokens(self) -> list:
        res = []
        for i, l in enumerate(self.lines):
            matching = re.finditer(TOKEN_PATTERN, l)
            res.extend([(i+1, m.start(0)+1, m.group(0)) for m in matching if m.group(0) != ' '])
        return res

    def analyze(self, show_tables=False):
        fields = ['TOKEN', 'DESCRIPTION', 'LINE', 'POSITION']
        tokens = self.get_tokens()

        identifiers = prettytable.PrettyTable()
        constants = prettytable.PrettyTable()
        operators = prettytable.PrettyTable()
        keywords = prettytable.PrettyTable()

        identifiers.title = 'IDENTIFIERS'
        constants.title = 'CONSTANTS'
        operators.title = 'OPERATORS'
        keywords.title = 'KEYWORDS'

        identifiers.field_names = fields
        constants.field_names = fields
        operators.field_names = fields
        keywords.field_names = fields

        for index, (line, position, token) in enumerate(tokens):
            if token in patterns.keywords:
                keywords.add_row([token, patterns.keywords[token], line, position])
                continue
            if token in patterns.operators:
                operators.add_row([token, patterns.operators[token], line, position])
                continue
            if token in patterns.data_types:
                keywords.add_row([token, patterns.data_types[token], line, position])
                continue
            _identifier = re.match(IDENTIFIER_PATTERN, token)
            _integer = re.match(INT_PATTERN, token)
            _float = re.match(FLOAT_PATTERN, token)
            _string = re.match(STRING_PATTERN, token)
            if _identifier:
                _constant = False
                _function = False
                try:
                    _constant = tokens[index-2][2] == 'const'
                except:
                    pass
                try:
                    _function = tokens[index+1][2] == '('
                except:
                    pass
                try:
                    _previous = tokens[index-1][2]
                    if _previous in patterns.data_types:
                        if token in self.identifiers:
                            self.errors = True
                            raise SyntaxError('Identifier is duplicated!', line, position)
                        if _function:
                            self.functions[token] = [_previous, 0]
                        else:
                            self.identifiers[token] = _previous
                    else:
                        if token not in self.identifiers and token not in self.functions:
                                self.errors = True
                                raise SyntaxError('Identifier is undefined!', line, position)
                    if _function:
                        identifiers.add_row([token, f'{IDENTIFIER_DESC} "{"const" if _constant else ""} "{self.functions[token]}"', line, position])
                    else:
                        identifiers.add_row([token, f'{IDENTIFIER_DESC}"{"const" if _constant else ""} "{self.identifiers[token]}"', line, position])
                    continue
                except IndexError:
                    if token in self.identifiers:
                        if _function:
                            identifiers.add_row([token, f'{IDENTIFIER_DESC} {"const " if _constant else ""} "{self.functions[token]}"', line, position])
                        else:
                            identifiers.add_row([token, f'{IDENTIFIER_DESC}"{"const" if _constant else ""} "{self.identifiers[token]}"', line, position])
                        continue
                    else:
                        self.errors = True
                        raise SyntaxError('Identifier is undefined!', line, position)
            if _integer:
                constants.add_row([token, 'const int', line, position])
                continue
            if _float:
                constants.add_row([token, 'const float', line, position])
                continue
            if _string:
                constants.add_row(([token, 'const string', line, position]))
                continue
            raise LexicalError(f'{token} is unsupported!', line, position)
        if show_tables:
            print(identifiers, '\n')
            print(constants, '\n')
            print(keywords, '\n')
            print(operators, '\n')
        _parser = Parser(tokens)
        _parser.parse(show=False)
        return tokens