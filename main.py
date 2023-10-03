from parser import Parser
from interpreter import Interpreter

file = open('tests/Handgun_fbx_6_1_ASCII.fbx', 'r')
parser = Parser(file.read())
interpreter = Interpreter(parser.tokenizer())
interpreter.interpreter()
print(str(interpreter.document_node.get('Definitions').get('ObjectType').value[1].nodes[0].value))
