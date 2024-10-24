class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                temp = self.find_min_value(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root

    def find_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
