class Solution:
    def dfs(self, node, leaves):
        if node is None:
            return leaves
        if node.left is None and node.right is None:
            leaves.append(node.val)
            return leaves
        leaves = self.dfs(node.left, leaves)
        leaves = self.dfs(node.right, leaves)
        return leaves

    def leafSimilar(self, root1, root2) -> bool:
        left_tree = self.dfs(root1, [])
        right_tree = self.dfs(root2, [])

        return left_tree == right_tree
