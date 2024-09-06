class Solution:
    def dfs(self, node, isl, sum):
        if node is None:
            return sum
        if node.left is None and node.right is None and isl:
            sum += node.val
            return sum
        sum = self.dfs(node.left, True, sum)
        sum = self.dfs(node.right, False, sum)
        return sum

    def sumOfLeftLeaves(self, root) -> int:
        return self.dfs(root, False, 0)
