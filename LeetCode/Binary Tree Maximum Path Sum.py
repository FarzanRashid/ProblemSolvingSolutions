# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return 0
        print(node.val)
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.result = max(self.result, node.val + left + right)
        return node.val + max(left, right)

# Time complexity = O(n) where n is the number of nodes in the binary tree
# Space complexity = O(h) where h is the height of the binary tree
