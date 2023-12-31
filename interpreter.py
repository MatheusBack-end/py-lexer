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
            key = self.consume(['identifier'])

            self.consume(['operator'])
            
            if self.consume_list(key):
                return True

            value = self.consume(['identifier', 'string'])

            if self.consume_list_in_values(key, value):
                return True
             
            if self.current_token.type == 'separator':
                value = self.values_by_separator(value)
                
                if self.consume_list_in_values_deriva(key, value):
                    return True

            node = Node(key.value, [value])
            node.nodes = []
            self.scope.nodes.append(node)

            return True

    def consume(self, token_types):
        if self.current_token.type in token_types:
            token = self.current_token
            self.current_token = self.next_token()
            return token
        
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

    def consume_list(self, key):
        if self.current_token.value == '{':
            list_scope = Node(key.value, '[list]')
            list_scope.nodes = []
            list_scope.previous_scope = self.scope

            self.scope.nodes.append(list_scope)
            self.scope = list_scope
            self.consume(['operator'])

            return True

        return False

    def consume_list_in_values(self, key, value):
        if self.current_token.value == '{':
            value_array = []
            value_array.append(value)
            list_scope = Node(key.value, '[list]')
            list_scope.nodes = []
            list_scope.previous_scope = self.scope
            value_array.append(list_scope)
            node = Node(key.value, value_array)
            node.nodes = []
            self.scope = list_scope
            self.consume(['operator'])

            return True

        return False


    def consume_list_in_values_deriva(self, key, value):
        if self.current_token.value == '{':
            list_scope = Node(key.value, '[list]')
            list_scope.nodes = []
            list_scope.previous_scope = self.scope
            value.append(list_scope)
            node = Node(key.value, value)
            node.nodes = []
            self.scope.nodes.append(node)
            self.scope = list_scope
            self.consume(['operator'])

            return True

        return False

    def values_by_separator(self, value):
        value_array = []
        value_array.append(value)

        while self.current_token.type == 'separator':
            self.consume(['separator'])
            value_array.append(self.consume(['identifier', 'string']))

        return value_array
        


