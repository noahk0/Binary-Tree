def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    tree, bfs = [], deque([root]) if root else None

    while bfs:
        tree.append(bfs[-1].val)

        for _ in range(len(bfs)):
            node = bfs.popleft()

            if node.left:
                bfs.append(node.left)

            if node.right:
                bfs.append(node.right)

    return tree
