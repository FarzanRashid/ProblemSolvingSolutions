class Solution:
    def __init__(self):
        self.first_tree = []
        self.second_tree = []
        self.output = []
    def dfs(self, node, values):
        if node is None:
            return
        self.dfs(node.left, values)
        values.append(node.val)
        self.dfs(node.right, values)
        return

    def getAllElements(self, root1, root2):
        self.dfs(root1, self.first_tree)
        self.dfs(root2, self.second_tree)
        i, j = 0, 0
        while i < len(self.first_tree) and j < len(self.second_tree):
            if self.first_tree[i] < self.second_tree[j]:
                self.output.append(self.first_tree[i])
                i += 1
            else:
                self.output.append(self.second_tree[j])
                j += 1
        self.output += self.first_tree[i:]
        self.output += self.second_tree[j:]
        return self.output