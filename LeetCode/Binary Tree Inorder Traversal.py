class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node is None:
                return result
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
            return result
        return dfs(root)
