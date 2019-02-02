# Find maximum (or minimum) in Binary Tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def maxNode(root):
    if root is None:
        return

    stack =[]
    stack.append(root)
    print(root.val)
    while len(stack) > 0:
        
        node = stack.pop(0)

        if node.left is not None:
            stack.append(node.left)
            print(node.left.val)

        if node.right is not None:
            stack.append(node.right)






if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.left.right = Node(7)
    root.right =Node(3)
    root.right.left =Node(5)
    root.right.right =Node(6)
    root.right.left.left =Node(8)
    root.right.left.right =Node(9)

    maxNode(root)