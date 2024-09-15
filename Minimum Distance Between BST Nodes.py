class Solution:
    def __init__(self):
        self.node_vals = []
        self.output = float('inf')
    def minDiffInBST(self, root) -> int:
        def list_populator(node):
            if node is None:
                return
            list_populator(node.left)
            self.node_vals.append(node.val)
            list_populator(node.right)
            return
        list_populator(root)
        i, j = 0, 1
        while j < len(self.node_vals):
            if self.node_vals[j] - self.node_vals[i] < self.output:
                self.output = self.node_vals[j] - self.node_vals[i]
            i += 1
            j += 1
        return self.output
