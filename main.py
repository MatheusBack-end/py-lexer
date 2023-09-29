from parser import Parser
from interpreter import Interpreter

file = open('tests/filetest', 'r')
parser = Parser(file.read())
interpreter = Interpreter(parser.tokenizer())
interpreter.interpreter()
