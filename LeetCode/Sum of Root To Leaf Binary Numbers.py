class Solution:
    def dfs(self, node, path, sum=0):
        if node is None:
            return sum
        if node.left is None and node.right is None:
            path += str(node.val)
            return int(path, 2)
        path += str(node.val)
        sum += self.dfs(node.left, path)
        sum += self.dfs(node.right, path)
        return sum
    def sumRootToLeaf(self, root) -> int:
        return self.dfs(root, "")
