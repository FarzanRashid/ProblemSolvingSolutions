class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        if root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        if root.left is None and root.right is None:
            return 1
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
