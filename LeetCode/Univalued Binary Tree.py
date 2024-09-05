class Solution:
    value = 0

    def dfs(self, node):
        if node is None:
            return True
        if node.val != Solution.value:
            return False
        return self.dfs(node.left) and self.dfs(node.right)

    def isUnivalTree(self, root) -> bool:
        Solution.Value = None
        if root is None:
            return True
        Solution.value = root.val
        return self.dfs(root)
