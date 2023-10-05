from token import Token
from node import Node

class FbxToObj():

    def __init__(self, fbx_node):
        self.fbx_node = fbx_node
        self.get_all(fbx_node)
        #self.fbx_to_mesh()

    def get_objects(self):
        return self.fbx_node.get('Objects')

    def fbx_to_mesh(self):
        objects = self.get_objects()

        print(objects.get("Model").value[0].value)

    def get_all(self, node): 
        if node.nodes == None:
            return

        for i in node.nodes:
            if i.value != '[list]':
                for v in i.value:
                    if isinstance(v, Node):
                        self.get_all(v)
                        continue

                    if isinstance(v, list):
                        for l in v:
                            print(str(l.value))

                        continue

                    print(str(v.value))

            self.get_all(i)
