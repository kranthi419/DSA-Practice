
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def is_balanced_bt(root: Node):

    def check_balanced(root):
        if root is None:
            return 0

        lh = check_balanced(root.left)
        if lh == -1:
            return -1

        rh = check_balanced(root.right)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    return check_balanced(root) != -1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print(is_balanced_bt(root))



