class Solution(object):
    def checkTree(self, root):
        if root is None:
            return False
        result = 0
        if root.left is not None:
            result += root.left.val
        if root.right is not None:
            result += root.right.val
        return result == root.val
