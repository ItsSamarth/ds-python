class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def deleteNode(self, key):
        temp = self.head

        if (temp.data is not None):
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key is not present in the linkedlist  then return

        if temp is None:
            return

        # unlink the previous node
        prev.next = temp.next
        temp = None

    def deleteSpecificPosition(self, position):
        if self.head is None:
            return

        temp = self.head

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                return

        # if position is more then the number of node
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        # Unlink the node from the linkedlist
        temp.next = None
        temp.next = next

    def deleteAll(self):
        current = self.head
        while current:
            nextRef = current.next
            del current.data
            current = nextRef


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(5)
    llist.push(9)
    llist.printLL()
    llist.deleteNode(3)
    print("Linked list after deleting 3")
    llist.printLL()
    llist.deleteSpecificPosition(2)
    print("Linkedlist after deleting node at 2nd position")
    llist.printLL()
    print("Delete everything")
    llist.deleteAll()
