class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def maxDepth(node):
    if node is None:
        return 0;

    else:
        leftHeight = maxDepth(node.left)
        rightHeight = maxDepth(node.right)

        if leftHeight > rightHeight:
            return leftHeight+1

        else:
            return rightHeight + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxDepth(root))