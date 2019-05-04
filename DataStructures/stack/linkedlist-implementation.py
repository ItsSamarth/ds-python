class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self, new_data):
        new_node = StackNode(new_data)
        new_node.next = self.head
        self.head = new_node
        print(new_data, "Pushed to stack")

    def pop(self):
        if(self.isEmpty()):
            return float("-inf")

        temp = self.head
        self.head = self.head.next
        popped = temp.data

        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.head.data


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(" popped from stack", (stack.pop()))
    print("Top element is  ", (stack.peek()))
