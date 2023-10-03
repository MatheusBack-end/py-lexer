from node import Node
from debug_nodes import DebugNodes

class Nodev():

    nodes = []
    value = None
    key   = None
    previous_scope = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Interpreter():

    tokens = []
    pos = 0
    current_token = None
    document_node = None
    scope = None

    def __init__(self, tokens):
        self.tokens = tokens
        self.document_node = Node('document_node', None)
    
    def interpreter(self):
        #for i in range(0, len(self.tokens), 1):
            #print(self.tokens[i].type)
            
        #return
        self.scope = self.document_node
        self.scope.nodes = []
        self.current_token = self.tokens[self.pos]

        while self.eat():
            pass

        DebugNodes(self.document_node)
    
    def next_token(self):
        self.pos += 1
        return self.tokens[self.pos]

    def return_scope(self):
        previous = self.scope.previous_scope
        
        if previous == None:
            self.scope = self.document_node

        self.scope = previous

    def eat(self):
        if self.current_token.type == 'eof':
            return False
        
        while self.current_token.value == '}':
            self.return_scope()
            self.consume(['operator'])

        print(self.current_token.type + ' -> ' + str(self.current_token.value) + ' ' + str(self.current_token.line))
        if self.current_token.type == 'identifier':
            key = self.current_token

            self.consume(['identifier'])
            self.consume(['operator'])
            
            if self.current_token.value == '{':
                new_scope = Node(key.value, '(array)')
                new_scope.nodes = []
                
                new_scope.previous_scope = self.scope
                self.scope.nodes.append(new_scope)
                self.scope = new_scope
                self.consume(['operator'])
                

                return True

            value = self.current_token.value
            self.consume(['identifier', 'string'])

            if self.current_token.value == '{':
                new_scope = Node(key.value, '(array)')
                new_scope.nodes = []

                new_scope.previous_scope = self.scope
                self.scope.nodes.append(new_scope)
                self.scope = new_scope
                self.consume(['operator'])

                return True
            
            #print(str(self.current_token.line))
            if self.current_token.type == 'separator':
                unique = value
                value = []
                value.append(unique)

                while self.current_token.type == 'separator':
                    self.consume(['separator'])
                    value.append(self.current_token.value)
                    self.consume(["identifier", 'string'])

                if self.current_token.value == '{':
                    new_scope = Node(key.value, '(array)')
                    new_scope.nodes = []

                    new_scope.previous_scope = self.scope
                    self.scope.nodes.append(new_scope)
                    self.scope = new_scope
                    self.consume(["operator"])

                    return True

            node = Node(key.value, value)
            node.nodes = []
            self.scope.nodes.append(node)

            return True

    def eval(self):
        pass

    def consume(self, token_types):
        for i in range(0, len(token_types), 1):
            if self.current_token.type == token_types[i]:
                self.current_token = self.next_token()
                return None
            else:
                if self.current_token.type == 'eof':
                    return None

        print('SyntaxError: expected \'' + str(token_types) + '\' -> ' + str(self.current_token.type) + ' line: ' + str(self.current_token.line))
        quit()

  
