class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()



s = Stack()
while True:
    print("Push <value> ")
    print("POP")
    print("quit")
    do = input("would you like to do? ").split()

    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('stack is empty')
        else:
            print('Popped value: ', s.pop())
    elif operation =='quit':
        break