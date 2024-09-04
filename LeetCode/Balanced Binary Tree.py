class Solution:
    balanced = True
    def dfs(self, node):
        if node is None:
            return 0
        left_subtree = 1 + self.dfs(node.left)
        right_subtree = 1 + self.dfs(node.right)
        if abs(left_subtree - right_subtree) > 1:
            Solution.balanced = False
        return max(left_subtree, right_subtree)
    def isBalanced(self, root) -> bool:
        Solution.balanced = True
        self.dfs(root)
        return Solution.balanced
