def dfs(node, val=""):
    result = 0

    if node.left is None and node.right is None:
        val += str(node.data)
        result += int(val, 2)
        return result

    val += str(node.data)
    if node.left is not None:
        result += dfs(node.left, val)

    if node.right is not None:
        result += dfs(node.right, val)

    return result


def sum_root_to_leaf(tree) -> int:
    result = 0

    if tree is None:
        return result

    return dfs(tree)
