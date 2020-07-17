"""Given a binary tree, return all paths from the root to leaves.

1. implement tree
2. recursively iterate through branches
3. ???
4. profit
"""


class Node:
    def __init__(
        self,
        value,
        left=None,
        right=None
    ):
        self.parent = None
        self.value = value
        self.left = left
        self.right = right

        if left:
            left.parent = self
        if right:
            right.parent = self


def path_to_top(node: Node):
    parent_node = node.parent
    res = [node.value]
    while parent_node:
        res = res + [parent_node.value]
        parent_node = parent_node.parent
    return list(reversed(res))


def find_paths(node: Node):
    is_leaf = (not node.left) and (not node.right)
    res = []

    if is_leaf:
        return path_to_top(node)
    if node.left:
        res.append(find_paths(node.left))
    if node.right:
        res.append(find_paths(node.right))

    return res


if __name__ == "__main__":
    pass
    my_tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    print(find_paths(my_tree))
