from parser import Parser
from interpreter import Interpreter
from fbx_to_obj import FbxToObj

file = open('tests/Handgun_fbx_6_1_ASCII.fbx', 'r')
parser = Parser(file.read())
interpreter = Interpreter(parser)
interpreter.interpreter()
FbxToObj(interpreter.document_node)
#print(str(interpreter.document_node.get('Definitions').get('ObjectType').value[1].nodes[0].value))
