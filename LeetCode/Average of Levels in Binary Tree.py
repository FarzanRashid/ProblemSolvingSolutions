from queue import Queue


class Solution:
    def averageOfLevels(self, root):
        result = []
        if root is None:
            return result
        q = Queue()
        q.put(root)
        while not q.empty():
            length = q.qsize()
            sum = 0
            next_level = []
            for _ in range(length):
                node = q.get()
                sum += node.val
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            result.append(sum / length)
        return result
