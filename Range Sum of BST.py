class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        result = 0
        if root is None:
            return 0
        if low <= root.val <= high:
            result += root.val
        result += self.rangeSumBST(root.left, low, high)
        result += self.rangeSumBST(root.right, low, high)
        return result
