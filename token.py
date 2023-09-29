class Token():

    type = None
    value = None
    line = 0

    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
