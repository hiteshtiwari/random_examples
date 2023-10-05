class listNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head):
    fast = head
    
    while fast and fast.next:
        head = head.next 
        fast = fast.next.next 
        
        if head is fast:
            return True
    return False

def hasCycle(head: Optional[ListNode]) -> bool:

        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next 
        return False