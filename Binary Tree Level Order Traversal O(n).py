def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    tree, order = [], deque([root]) if root else None

    while order:
        level = []

        for _ in range(len(order)):
            node = order.popleft()
            level.append(node.val)

            if node.left:
                order.append(node.left)

            if node.right:
                order.append(node.right)

        tree.append(level)

    return tree
