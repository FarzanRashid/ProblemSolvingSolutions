class Solution:
    value = None
    def dfs(self, node, target, depth):
        if node.left is not None:
            if node.left.val == target:
                Solution.value = (node.val, depth + 1)
                return Solution.value
            self.dfs(node.left, target, depth + 1)

        if node.right is not None:
            if node.right.val == target:
                Solution.value = (node.val, depth + 1)
                return Solution.value
            self.dfs(node.right, target, depth + 1)
        return Solution.value

    def isCousins(self, root, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False

        Solution.value = None
        x_val, x_depth = self.dfs(root, x, 0)
        y_val, y_depth = self.dfs(root, y, 0)
        if x_val != y_val and y_depth == x_depth:
            return True
        return False
