from token import Token
from parser_utils import ParserUtils

class Parser(ParserUtils):

    text = None
    pos = 0
    line = 0
    
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
