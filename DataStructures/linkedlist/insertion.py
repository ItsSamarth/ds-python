class Node:
    # function to initilize node object
    def __init__(self, data):
        self.data = data #Assign Data
        self.next = None #Initilize Next data null

class LinkedList:

    #function to initilize linkedlist object
    def __init__(self):
        self.head =None

    #Function to insert node at the beginning
    def insertFront(self, new_data):
        new_node = Node(new_data)

        # make next of new node as head
        new_node.next = self.head

        #move the head to point to new Node
        self.head = new_node

    #Function to Inserts a new node after the given prev_node
    def insertAfterSpecificNode(self, prev_node, new_data):
        #check the given node exists
        if prev_node is None:
            print("The given node must be in linkedlist")
        return

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while(current.next):
            current = current.next

        current.next = new_node

    #Function to print linkedlist
    def printList(self):
        current = self.head
        while(current.next):
            print(current.data)
            current = current.next


if __name__ == '__main__':

    #start with empty list
    linkedlist = LinkedList()

    # linkedlist.insertAtEnd(6)
    # linkedlist.insertFront(7)
    # linkedlist.insertFront(1)
    linkedlist.insertAtEnd(4)

    # linkedlist.insertAfterSpecificNode(linkedlist.head.next, 8)

    print("Created linkedlist is:")
    linkedlist.printList()
