from token import Token

class Parser():

    text = None
    pos = 0
    line = 0

    OPERATOR = ['{', '}', ':']
    STRING = ['"', "'"]
    ALPHANUM = ['-', '_', '.', '*']
    IGNORE = [' ', '\t', '\r']
    GLOBAL_IGNORE = [' ', '\t', '\r', '\n', ';']
    
    def __init__(self, text):
        self.text = text

    def get_next_token(self):
        char = self.ignore_whitespace(self.text[self.pos])

        if self.pos > len(self.text) -1:
            return Token('eof', len(self.text), self.line)
        
        if char.isalnum() or char in self.ALPHANUM:
            return self.get_identifier(char)

        if char in self.OPERATOR:
            self.consume_char()
            return Token('operator', char, self.line)

        if char in self.STRING:
            return self.get_string()

        if char == ',':
            self.consume_char()
            return Token('separator', char, self.line)

        self.parser_error(char)

    def get_string(self):
        char = self.consume_char()
            
        string = ''

        while char != '"':
            string += char
            char = self.consume_char()

        self.consume_char()

        return Token('string', string, self.line)

    def get_identifier(self, char):
        identifier = ''
        
        while char.isalnum() or char in self.ALPHANUM:
            identifier += char
            char = self.consume_char()

        return Token('identifier', identifier, self.line)


    def consume_char(self):
        self.pos += 1
        
        if self.pos > len(self.text) -1:
            return None

        return self.text[self.pos]

    def ignore_whitespace(self, char):
        while char in self.IGNORE:
            char = self.consume_char()

        if char == ';':
            while char != '\n':
                char = self.consume_char()

        if char == '\n':
            self.line += 1
            char = self.consume_char()

        if char in self.GLOBAL_IGNORE:
            return self.ignore_whitespace(char)

        return char

    def parser_error(self, char):
        print("parser error " + str(bytes(char, 'ascii')) + ' ' + str(self.line))
        quit(1)
