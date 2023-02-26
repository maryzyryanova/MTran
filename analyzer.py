import re
from patterns import (
    TOKEN_PATTERN
)

class Analyzer(object):
    def __init__(self, source) -> None:
        self.lines = source.split('\n')
        self.identidiers = {}
        self.errors = False
        self.functions = {
            'read': ['string', 0], 
            'readint': ['int', 0],
            'readfloat': ['float', 0],
            'sqrt': ['float', 1],
            'pow': ['int', 2]
        }
    
    def get_tokens(self) -> list:
        res = []
        for i, l in enumerate(self.lines):
            matching = re.finditer(TOKEN_PATTERN, l)
            res.extend([(i+1, m.start(0)+1, m.group(0)) for m in matching if m.group(0) != ' '])
        return res