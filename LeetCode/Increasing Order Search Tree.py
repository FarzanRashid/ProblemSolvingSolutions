class Solution:
    def __init__(self):
        self.result = None
        self.chamaleon = None

    def increasingBST(self, root):
        if root is None:
            return
        self.increasingBST(root.left)
        if self.result is None:
            self.result = root
            self.chamaleon = root
        else:
            self.chamaleon.right = root
            self.chamaleon = root
        self.chamaleon.left = None
        self.increasingBST(root.right)
        return self.result
