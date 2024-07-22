from typing import List
from queue import Queue


# def dfs(result, node, level):
#     if node is None:
#         return
#     elif len(result) == level:
#         result.append([])
#     result[level].append(node.data)
#     dfs(result, node.left, level + 1)
#     dfs(result, node.right, level + 1)
#
#
# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     result = []
#     level = 0
#
#     dfs(result, tree, level)
#     return result


def binary_tree_depth_order(tree) -> List[List[int]]:
    result = []
    if tree is None:
        return result
    q = Queue()
    q.put(tree)
    while not q.empty():
        result.append([])
        q_size = q.qsize()
        for _ in range(q_size):
            node = q.get()
            result[-1].append(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
    return result
