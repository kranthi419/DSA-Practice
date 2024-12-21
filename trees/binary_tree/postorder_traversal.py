
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    postorder_traversal(root)


if __name__ == "__main__":
    main()
