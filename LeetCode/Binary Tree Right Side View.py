# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = Queue()
        q.put(root)
        while not q.empty():
            result.append(q.queue[-1].val)
            for _ in range(q.qsize()):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return result


# Time complexity = O(n) where n is the number of nodes in the binary tree
# Space complexity = O(n) where n is the number of nodes in the binary tree
