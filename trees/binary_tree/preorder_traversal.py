
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    preorder_traversal(root)


if __name__ == '__main__':
    main()
