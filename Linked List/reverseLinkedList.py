head = [1,2,3,4,5]

def reverseLinkedList(head):  # iterative approch, most optimal time complexity is O(n) as we are iterating but space complexity is O(1)
    prev = None
    curr = head

    while curr != None:
        temp_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node
    return prev

print(reverseLinkedList(head))
