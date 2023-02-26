class LexicalError(Exception):
    def __init__(self, message, line, position):
        super().__init__(f'LEXICAL ERROR | line: {line}, position: {position} | {message}')

class SyntaxError(Exception):
    def __init__(self, message, line, position):
        super().__init__(f'SYNTAX ERROR | line: {line}, position: {position} | {message}')

class SemanticsError(Exception):
    def __init__(self, message, line, position):
        super().__init__(f'SEMANTICS ERROR | line: {line}, position: {position} | {message}')