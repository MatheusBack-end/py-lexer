from token import Token

class Parser():

    text = None
    pos = 0
    line = 0
    
    def __init__(self, text):
        self.text = text


    def tokenizer(self):
        tokens = []
        
        token = self.get_next_token()

        while token.type != 'eof':
            tokens.append(token)
            token = self.get_next_token()
        
        tokens.append(token)

        return tokens

    def get_next_token(self):
        if self.pos > len(self.text) -1:
            return Token('eof', len(self.text), self.line)

        char = self.text[self.pos]
        
        if char.isalnum():
            identifier = ''
        
            while(char.isalnum()):
                identifier += char
                char = self.consume_char()

            return Token('identifier', identifier, self.line)

        if char == ':':
            token = Token('operator', ':', self.line)
            self.consume_char()
            
            return token

        if char == '{':
            token = Token('operator', '{', self.line)
            self.consume_char()

            return token

        if char == '}':
            token = Token('operator', '}')
            self.consume_char()

            return token

        if char == '"':
            char = self.consume_char()
            
            string = ''

            while char != '"':
                string += char
                char = self.consume_char()

            self.consume_char()

            return Token('string', string, self.line)

        if char == '\n':
            self.line += 1
            self.consume_char()
            return self.get_next_token()

        if char == ' ':
            self.consume_char()
            return self.get_next_token()

        print('unespected token', char)
        quit(1)


    def consume_char(self):
        self.pos += 1
        
        if self.pos > len(self.text) -1:
            return None

        return self.text[self.pos]
