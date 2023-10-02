class DebugNodes():

    text = None
    node = None
    index = 0

    def __init__(self, main_node):
        self.main_node = main_node
        self.node = main_node
        self.debug(0)

    def debug(self, index):
        i = index 
        for i in range(index, len(self.node.nodes), 1):

            if len(self.node.nodes[i].nodes) > 0:
                print(self.node.nodes[i].key + ' [list] —→ ' + self.node.key)
                self.node = self.node.nodes[i]
                self.index = i + 1
                self.debug(0)
                
            else:
                log = self.node.nodes[i].key + ' —→ ' + str(self.node.key)

                print(log)
                pass

        
        if self.node.previous_scope != None:
            self.node = self.node.previous_scope
            self.debug(self.index)

