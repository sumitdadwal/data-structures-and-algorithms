class Stack():
    def __init__(self):
        self.arr = []
        self.minStack = []

    def peek(self):
        if len(self.arr) == 0:
            print('Empty Stack')
        else:
            return self.arr[-1]
    
    def push(self, data):
        self.arr.append(data)
        if self.minStack:
            data = min(data, self.minStack[-1])
        data = data
        self.minStack.append(data)
        return

    def pop(self):
        if len(self.arr) == 0:
            print('Empty Stack')
        else:
            self.arr.pop()
            self.minStack.pop()
        return

    def getMin(self):
        return self.minStack[-1]
    
    def print_stack(self):
        for i in range(len(self.arr)-1, -1, -1):
            print(self.arr[i], end=' < ')

    


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(-1)
s.print_stack()

print(s.getMin())
