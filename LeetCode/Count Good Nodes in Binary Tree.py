# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.vals = [root.val]
        self.dfs(root, root.val)
        return self.result

    def dfs(self, node, value):
        if node is None:
            return
        if node.val >= value:
            self.result += 1
        value = node.val
        self.dfs(node.left, value)
        self.dfs(node.right, value)

# Time complexity = O(n) where n is the number of nodes in the binary tree
# Space complexity = O(h) where h is the height of the binary tree
