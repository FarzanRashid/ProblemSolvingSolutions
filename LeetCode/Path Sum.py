class Solution:
    def dfs(self, node, target, value = 0):
        if node is None:
            return False
        value += node.val
        if node.left is None and node.right is None:
            return value == target
        return self.dfs(node.left, target, value) or self.dfs(node.right, target, value)
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root, targetSum)
