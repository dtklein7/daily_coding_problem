"""Problem596: reverse a binary tree

I think recursion will be my friend here!
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

    def __repr__(self):
        return self.value

    def __str__(self):
        return f'  {self.value}\n /  \\ \n{self.left}    {self.right}'


TEST_CASES = [
    TreeNode(
        "a", TreeNode("b", TreeNode("d"), TreeNode("e")), TreeNode("c", TreeNode("f"))
    )
]


def reverse_tree(node):
    if node is None:
        return node

    temp = node.left
    node.left = reverse_tree(node.right)
    node.right = reverse_tree(temp)
    return node


if __name__ == "__main__":
    for test_case in TEST_CASES:
        tree = reverse_tree(test_case)
