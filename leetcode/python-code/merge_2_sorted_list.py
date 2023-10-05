class ListNode():
    def __init__(self, val, next):
        self.val = val
        self.next = next
        
def mergeTwoSortedList(l1, l2):
    head = ListNode()
    current = head
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next 
        else:
            current.next = l2
            l2 = l2.next 
            
        current = current.next
    current.next = l1 or l2
    
    return head.next 

list_1 = []