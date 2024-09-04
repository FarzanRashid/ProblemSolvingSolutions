class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(node):
            if node is None:
                return result
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return result
        return dfs(root)
