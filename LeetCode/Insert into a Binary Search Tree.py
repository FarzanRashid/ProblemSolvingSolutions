class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None:
            return TreeNode(val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
