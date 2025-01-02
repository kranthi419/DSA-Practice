
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root: Node):
    if root is None:
        return

    stack = [root]

    while len(stack) > 0:
        node = stack.pop()
        print(node.data)

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(4)

    inorder_traversal(root)

