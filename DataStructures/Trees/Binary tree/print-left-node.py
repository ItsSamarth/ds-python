# Print Left View of a Binary Tree

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printLeftView(root):
    if root is None:
        return 0
    result = root.val
    leftmax  =printLeftView(root.left) 
    rightmax =printLeftView(root.right)

    print("Result", result)
    print("leftmax ", leftmax)
    print("Rightmax", rightmax)

    if leftmax > result:
        result =leftmax
    if rightmax > result:
        result = rightmax
    return result
    





if __name__ == "__main__":
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)

    print("Maximum element is" , printLeftView(root))