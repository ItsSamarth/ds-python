#Print Ancestors of a given node in Binary Tree
''' Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.
For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printAncestor(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    #if target is present in either right or left sub tree then print the node

    if printAncestor(root.left , target) or printAncestor(root.right , target):
        print(root.val)
        return True


    return False



root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

printAncestor(root, 7)