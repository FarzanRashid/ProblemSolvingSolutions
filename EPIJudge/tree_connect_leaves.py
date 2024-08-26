# Time complexity O(N) where N is the number of nodes.

def dfs(node, result):
    if node is None:
        return result
    if node.left is None and node.right is None:
        result.append(node)
        return result
    dfs(node.left, result)
    dfs(node.right, result)
    return result


def create_list_of_leaves(tree):
    result = []
    return dfs(tree, result)

# def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
#     result = []
#     if tree is None:
#         return result
#
#     q = Queue()
#     q.put(tree)
#
#     while not q.empty():
#         node = q.get()
#         if node.left is None and node.right is None:
#             result.append(node)
#         if node.left is not None:
#             q.put(node.left)
#         if node.right is not None:
#             q.put(node.right)
#     return result
