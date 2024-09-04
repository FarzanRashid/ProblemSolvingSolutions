class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return 1 + self.maxDepth(root.right)
        if root.right is None and root.left is not None:
            return 1 + self.maxDepth(root.left)
        if root.left is None and root.right is None:
            return 1
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
