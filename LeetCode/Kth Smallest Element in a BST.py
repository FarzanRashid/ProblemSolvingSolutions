class Solution:
    def __init__(self):
        self.values = []

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        self.values.append(node.val)
        self.dfs(node.right)

    def kthSmallest(self, root, k: int) -> int:
        self.dfs(root)
        return self.values[k - 1]
