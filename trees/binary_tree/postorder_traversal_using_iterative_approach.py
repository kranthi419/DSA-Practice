
class Node:
    def __init__(self, data = None):
        self.data =  data
        self.left = None
        self.right = None


def postorder_traversal(root: Node):
    if root is None:
        return

    stack_1 = [root]
    stack_2 = []

    while len(stack_1) > 0:
        node = stack_1.pop()
        stack_2.append(node)
        if node.left is not None:
            stack_1.append(node.left)
        if node.right is not None:
            stack_1.append(node.right)

    while len(stack_2) > 0:
        node = stack_2.pop()
        print(node.data)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    postorder_traversal(root)
