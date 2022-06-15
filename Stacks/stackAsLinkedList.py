

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.length == 0:
            print("Stack Empty")
        return self.top.data

    def push(self, data):
        newNode = Node(data)
        if self.length == None:
            self.bottom = newNode
            self.top =self.bottom
            self.length += 1
        else:
            newNode.next = self.top
            self.top = newNode
            self.length += 1
    
    def pop(self):
        if self.length == 0:
            print("Empty Stack")
        else:
            self.top = self.top.next
            self.length -= 1

    def print_stack(self):
        if self.top == None:
            print("Empty Stack")
        else:
            current_pointer = self.top
            while current_pointer != None:
                print(current_pointer.data, end= " < " )
                current_pointer = current_pointer.next
            print()


s = Stack()


s.push('Shopify')
s.push('Google')
s.push('Microsoft')
s.push('Facebook')
s.push('IBM')
s.push('Spotify')
s.print_stack()
# print(f'TOP = {s.top.data}')
# s.pop()
# s.print_stack()
print(s.peek())

