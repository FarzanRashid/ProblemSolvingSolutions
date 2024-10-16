class Solution:
    def __init__(self):
        self.p_path = []
        self.q_path = []

    def dfs(self, node, target, path):
        if node.val == target.val:
            path.append(node)
            return path
        if node is None:
            return path
        path.append(node)
        if node.val < target.val:
            self.dfs(node.right, target, path)
        if node.val > target.val:
            self.dfs(node.left, target, path)
        return path

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = self.dfs(root, p, self.p_path)
        self.q_path = self.dfs(root, q, self.q_path)
        min_route = min(len(self.p_path), len(self.q_path))
        self.p_path = self.p_path[:min_route]
        self.q_path = self.q_path[:min_route]
        while self.p_path:
            if self.p_path[-1].val == self.q_path[-1].val:
                return self.p_path[-1]
            else:
                self.p_path.pop()
                self.q_path.pop()
