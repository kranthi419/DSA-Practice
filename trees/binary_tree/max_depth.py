
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def max_depth(root: Node):
    if root is None:
        return 0

    lh = max_depth(root.left)
    rh = max_depth(root.right)

    return 1 + max(lh, rh)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(max_depth(root))