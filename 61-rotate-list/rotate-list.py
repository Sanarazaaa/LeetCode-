class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Handle edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Step 2: Find the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 3: Optimize k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head  # No rotation needed
        
        # Step 4: Find the new tail (length - k - 1) and new head
        current = head
        for _ in range(length - k - 1):  # Move to the new tail
            current = current.next
        
        new_head = current.next  # New head of the rotated list
        current.next = None  # Break the list to form the new tail
        
        # Step 5: Connect the old tail to the old head
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        return new_head
