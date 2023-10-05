class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def reverseList(head):
    new_list = None
    current = head
    
    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node
    return new_list

# A = ListNode(1, 2)
# B = ListNode(2,3)
# C = ListNode(3,4)
# D = ListNode(4, 5)
# E = ListNode(5, None)
# print(E)

res = reverseList(A)
print(res)