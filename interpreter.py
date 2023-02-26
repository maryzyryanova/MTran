from analyzer import Analyzer

class Interpreter(object):
   def load(self, src_path):
       with open(src_path, 'r') as f:
           self.source = f.read()
           self.analyzer = Analyzer(self.source)

   def analyze(self):
       try:
           self.tokens = self.analyzer.analyze(show_token_tables=True)
       except Exception as e:
           print(e)