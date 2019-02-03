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

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
            
        return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)
    ll.push(60)
    ll.printll()
    print("Checking loop in linkedlist")
    ll.head.next.next.next.next = ll.head
    if(ll.detectLoop()):
        print("Loop found")
    else:
        print("Not Found")
    