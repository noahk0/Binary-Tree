def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return None

    i = inorder.index(preorder[0])

    return TreeNode(preorder.pop(0), self.buildTree(preorder, inorder[:i]), self.buildTree(preorder, inorder[i + 1:]))
