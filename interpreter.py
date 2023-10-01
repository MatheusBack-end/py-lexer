class Node():

    nodes = []
    value = None
    key   = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Interpreter():

    tokens = []
    pos = 0
    current_token = None
    document_node = None

    def __init__(self, tokens):
        self.tokens = tokens
        self.document_node = Node('document_node', None)
    
    def interpreter(self):
        self.current_token = self.tokens[self.pos]

        while self.eat():
            pass

        for o in range(0, len(self.document_node.nodes), 1):
            print(self.document_node.nodes[o].value)
    
    def next_token(self):
        self.pos += 1
        return self.tokens[self.pos]

    def eat(self):
        if self.current_token.type == 'eof':
            return False

        if self.current_token.type == 'identifier':
            key = self.current_token

            self.consume(['identifier'])
            self.consume(['operator'])

            value = self.current_token
            self.consume(['identifier', 'string'])

            node = Node(key.value, value.value)
            self.document_node.nodes.append(node)

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

  
