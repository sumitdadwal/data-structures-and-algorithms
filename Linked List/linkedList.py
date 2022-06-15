class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return "Empty Linked List"
        else:
            return self.tail.data

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def pop(self):
        if self.length == 0:
            return "Empty Linked List"

        curr_node = self.head
        index = self.length
        for i in range(index - 1):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        if curr_node.next == None:
            self.tail = curr_node
            self.length -= 1

    def removebyindex(self, index):
        if self.length == 0:
            return "Empty Linked List"

        if index == 0:
            self.head = self.head.next
            self.length -= 1

        elif index <= self.length:
            curr_node = self.head
            for i in range(index - 1):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
            self.length -= 1
            if curr_node.next == None:
                self.tail = curr_node
                self.length -= 1
        
        else:
            self.pop()

    def insert(self, index, data):
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        elif index >= self.length:
            if index > self.length:
                print("Invalid index. Adding value to the end")
            self.append(data)
        else:
            curr_node = self.head
            for i in range(index-1):
                curr_node = curr_node.next
            newNode.next = curr_node.next
            curr_node.next = newNode
            self.length += 1

    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        newNode.next = self.head
        self.head = newNode
        self.tail = self.head
        self.length += 1

    def print_list(self):
        if self.head == None:
            print('Empty Linked List')

        else:
            curr_node = self.head
            while curr_node != None:
                print(curr_node.data, end= ' -> ')
                curr_node = curr_node.next
        print()
    def length(self):
        return self.length

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(5)
l.append(6)
l.append(7)
l.insert(3, 4)
# l.insert(3000, 4568)
l.removebyindex(0)

print(l.length)
l.print_list()
        
        