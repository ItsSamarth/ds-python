class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def insertAtPosition(root, key_node, next_node):
    temp = root
    new_node = Node(next_node)
    while temp != None:
        print('root', temp.val, 'search node', key_node, ' new node', new_node)
        print('Root becomes', temp.val)
        if temp.left is None:
            temp.left = new_node
        elif temp.right is None:
            temp.right = new_node
        else:
            temp = temp.right
            return
        # if temp.left.val == key_node:
        #     temp = temp.left
        # elif temp.right.val == key_node:
        #     temp = temp.right
        # elif temp.val == key_node:
        #     insertNode(temp, new_node)
        # else:
        #     temp = temp.right


def insertNode(temp, new_node):
    if temp.left is None:
        temp.left = new_node
    else:
        temp.right = new_node
    return


def printInorder(root):
    if root:
        printInorder(root.left)
        printInorder(root.val)
        printInorder(root.right)


if __name__ == "__main__":
    tc = 7
    keys = [-1, 1, 1, 3, 3, 4, 4]
    count = 2
    root = Node(1)
    for i in range(1, tc):
        # print(root.val, keys[i], count)
        # printInorder(root)
        print('brain fuck', root, keys[i], count)
        print(insertAtPosition(root, keys[i], count))
        count += 1
    print('Inorder recursion')
    printInorder(root)
