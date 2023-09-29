class Interpreter():

    tokens = []
    current_token = None
    pos = 0
    keys = []
    values = []

    def __init__(self, tokens):
        self.tokens = tokens
    
    def interpreter(self):
        self.current_token = self.tokens[self.pos]

        while self.current_token.type != 'eof':
            if self.current_token.type == 'identifier':
                key = self.current_token
                self.consume(['identifier'])

                self.consume(['operator'])
                value = self.current_token

                self.consume(['identifier', 'string'])

                self.keys.append(key.value)
                self.values.append(value.value)

        print(self.keys, self.values)
    
    def next_token(self):
        self.pos += 1
        return self.tokens[self.pos]
        
    def consume(self, token_types):
        for i in range(0, len(token_types), 1):
            if self.current_token.type == token_types[i]:
                self.current_token = self.next_token()
                return None
        
        print('SyntaxError: expected \'' + str(token_types) + '\' -> ' + self.current_token.type + ' line: ' + str(self.current_token.line))
        quit()

  
