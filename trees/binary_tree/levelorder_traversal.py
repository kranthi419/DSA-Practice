
class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def levelorder_traversal(root):
    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    levelorder_traversal(root)


if __name__ == '__main__':
    main()
