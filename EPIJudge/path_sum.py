# Time complexity O(V + E), where V is the number of nodes and E is number of edges.
def dfs(node, target, val=0):
    if node is None:
        return False

    if node.left is None and node.right is None:
        val += node.data
        return val == target
    val += node.data

    return dfs(node.left, target, val) or dfs(node.right, target, val)


def has_path_sum(tree, remaining_weight: int) -> bool:
    return dfs(tree, remaining_weight)
