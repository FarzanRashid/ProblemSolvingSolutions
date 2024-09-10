class Solution:
    def dfs(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.right)
    def isSubtree(self, root, subRoot) -> bool:
        if root is None and subRoot is not None:
            return False
        if root is not None and subRoot is None:
            return False
        if root.val == subRoot.val:
            result = self.dfs(root, subRoot)
            if result:
                return True
        left_tree = self.isSubtree(root.left, subRoot)
        if left_tree:
            return True
        return self.dfs(root.right, subRoot.right)
