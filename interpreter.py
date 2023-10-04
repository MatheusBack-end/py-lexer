"""
simple key and value 
    [identifier][operator -> ':'][identifier, string]

multiples values 
    [identifier][operator -> ':'][identifier, string][separator][etc..]

array value 
    [identifier][operator -> ':'][operator -> '{'][etc..][operator -> '}']

value and array 
    [identifier][operator -> ':'][identifier, string][operator -> '{'][etc..][operator -> '}']

multiples values and array 
    [identifier][operator -> ':'][identifier, string][separator][etc..][operator -> '{'][etc..][operator -> '}']

"""

from node import Node

class Interpreter():

    tokens = []
    pos = 0
    current_token = None
    document_node = None
    scope = None

    def __init__(self, parser):
        self.parser = parser
        self.document_node = Node('document_node', None)
    
    def interpreter(self):
        self.scope = self.document_node
        self.scope.nodes = []
        self.current_token = self.next_token()

        while self.eat():
            pass
    
    def next_token(self):
        return self.parser.get_next_token()

    def return_scope(self):
        previous = self.scope.previous_scope
        
        if previous == None:
            self.scope = self.document_node

        self.scope = previous

    def close_scopes(self):
        while self.current_token.value == '}':
            self.consume(['operator'])
            self.return_scope()

    def eat(self):
        if self.end_tokens():
            return False

        self.close_scopes()

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
                unique = value
                value = []
                value.append(unique)
                new_scope = Node(key.value, '(array)')
                new_scope.nodes = []

                new_scope.previous_scope = self.scope
                node = Node(key.value, value)
                node.nodes = []
                self.scope.nodes.append(node)
                value.append(new_scope)
                self.scope = new_scope
                self.consume(['operator'])

                
                return True
            
            if self.current_token.type == 'separator':
                unique = value
                value = []
                value.append(unique)

                while self.current_token.type == 'separator':
                    self.consume(['separator'])
                    value.append(self.current_token.value)
                    self.consume(["identifier", 'string'])

                #print(value)

                if self.current_token.value == '{':
                    new_scope = Node(key.value, '[array]')
                    new_scope.nodes = []
                    
                    new_scope.previous_scope = self.scope
                    self.scope = new_scope
                    value.append(new_scope)
                    self.consume(["operator"])

                    node = Node(key.value, value)
                    node.nodes = []
                    self.scope.previous_scope.nodes.append(node)

                    return True

            node = Node(key.value, value)
            node.nodes = []
            self.scope.nodes.append(node)

            return True

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

    def end_tokens(self):
        if self.current_token.type == 'eof':
            return True

        return False

    def get_simple_node(self, node):
        pass

    def get_list(self, key):
        pass
