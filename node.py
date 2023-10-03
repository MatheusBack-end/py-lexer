class Node():

    nodes = None
    key = None
    value = None
    previous_scope = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get(self, key):
        for i in range(0, len(self.nodes), 1):
            node = self.nodes[i]

            if node.key == key:
                return node
