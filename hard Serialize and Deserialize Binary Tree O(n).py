class Codec:

    def serialize(self, root):
        serial = []

        def dfs(node):
            if node:
                serial.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                serial.append('!')

        dfs(root)
        
        return ' '.join(serial)
        

    def deserialize(self, data):
        self.i, data = 0, iter(data.split())

        def dfs():
            val = next(data)

            if val == '!':
                return
                
            root = TreeNode(val)
            root.left, root.right = dfs(), dfs()

            return root

        return dfs()
