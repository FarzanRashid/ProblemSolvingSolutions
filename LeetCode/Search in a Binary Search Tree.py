class Solution:
    def searchBST(self, root, val: int):
        result = None
        if root is None:
            return result
        if root.val == val:
            return root
        if root.val > val:
            result = self.searchBST(root.left, val)
        if root.val < val:
            result = self.searchBST(root.right, val)
        return result
