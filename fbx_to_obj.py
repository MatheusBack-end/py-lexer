class FbxToObj():

    def __init__(self, fbx_node):
        self.fbx_node = fbx_node
        self.fbx_to_mesh()

    def get_objects(self):
        return self.fbx_node.get('Objects')

    def fbx_to_mesh(self):
        objects = self.get_objects()

        print(objects.get("Model").value[0].value)
