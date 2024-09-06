class Solution:
    def evaluateTree(self, root) -> bool:
        if root.val  < 2:
            return root.val
        left_tree = self.evaluateTree(root.left)
        right_tree = self.evaluateTree(root.right)

        if root.val == 3:
            return left_tree and right_tree
        return left_tree or right_tree
