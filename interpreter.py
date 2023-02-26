from analyzer import Analyzer
from subprocess import call
import os

class Interpreter(object):
    def load(self, src_path):
        self.src_path = src_path
        with open(src_path, 'r') as f:
            self.source = f.read()
            self.analyzer = Analyzer(self.source)
            self.errors = False

    def analyze(self):
        try:
            self.identifiers, self.functions, self.ast = self.analyzer.analyze(show_token_tables=False)
        except Exception:
            print(Exception)
        self.errors = self.analyzer.errors

    def run(self):
        with open('data', 'r') as file:
            data = file.read()
            self.source = data + '\n' + self.source
        with open('bytecode.c', 'w') as bytecode_file:
            bytecode_file.write(self.source)
        call(['g++', '-Wall', os.path.abspath('bytecode.c'), '-o', os.path.abspath('output'), '-lm'])
        call('./output')