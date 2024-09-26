class Solution:
    def __init__(self):
        self.values = []
    def isValidBST(self, root) -> bool:
        if root is None:
            return
        self.isValidBST(root.left)
        self.values.append(root.val)
        self.isValidBST(root.right)
        i, j = 0, 1
        while j < len(self.values):
            if self.values[i] >= self.values[j]:
                return False
            i += 1
            j += 1
        return True
