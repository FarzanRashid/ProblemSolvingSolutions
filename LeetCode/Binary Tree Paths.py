class Solution:
    def dfs(self, node, paths, path):
        if node is None:
            return path
        if node.left is None and node.right is None:
            path += str(node.val)
            paths.append(path)
            return paths
        path += str(node.val) + "->"
        self.dfs(node.left, paths, path)
        self.dfs(node.right, paths, path)
        return paths

    def binaryTreePaths(self, root):
        return self.dfs(root, [], "")
