class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    
    if root is None:
        return 

    s =[]
    s.append(root)
    current = root.left
    done = False
    while done == False:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if len(s) > 0 :
                popped = s.pop()
                print(popped.val)
                current = popped.right
            
            else:
                done = True

            


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    printInorder(root)
