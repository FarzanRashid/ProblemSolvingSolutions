class Solution:
    def __init__(self):
        self.value = 0
    def convertBST(self, root):
        if root is None:
            return
        self.convertBST(root.right)
        root.val += self.value
        self.value = root.val
        self.convertBST(root.left)
        return root
