class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def inser(root, key, new_node):
    print(root.data, key, new_node)
    if key == -1:
        root = new_node

    while root != None:
        print(root.data)
        # Traverse until reaches to dead end
        if key > root.data:
            print('coming in if')
            root = root.right
        elif key < root.data:
            print('coming in elseif')
            root = root.left
        else:
            print('coming in else')
            if new_node > root.data:
                root.right = new_node
                return
            else:
                root.left = new_node
                print(new_node, " is inserted")
                return
    return False


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__ == "__main__":
    tc = 7
    keys = [-1, 1, 1, 3, 3, 4, 4]
    count = 2
    root = Node(1)
    for i in range(1, tc):
        # print(root.data, keys[i], count)
        inser(root, keys[i], count)
        count += 1
    print("Inorder traversal of binary tree")
    inorder(root)
    print(root)
