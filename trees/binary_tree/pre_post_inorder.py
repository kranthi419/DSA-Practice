
class Node:
    def __init__(self, data = None):
        self.data =  data
        self.left = None
        self.right = None


def pre_post_inorder_traversal(root: Node):
    pre_order = []
    post_order = []
    inorder = []

    stack = [(root,1)]
    while len(stack) > 0:
        node, num = stack[-1]
        if num == 1:
            pre_order.append(node.data)
            stack[-1] = node, 2
            if node.left is not None:
                stack.append((node.left, 1))
        elif num == 2:
            inorder.append(node.data)
            stack[-1] = node, 3
            if node.right is not None:
                stack.append((node.right, 1))
        else:
            post_order.append(node.data)
            stack.pop()
    print(pre_order)
    print(inorder)
    print(post_order)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)

    pre_post_inorder_traversal(root)