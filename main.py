from interpreter import Interpreter

interpreter = Interpreter()
interpreter.load('/Users/mariazyryanova/Desktop/BSUIR/3 course/MTran/files/input.txt')
interpreter.analyze()

if not interpreter.errors:
    interpreter.run()