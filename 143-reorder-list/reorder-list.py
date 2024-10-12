# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorder the linked list in-place using a stack.
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: # this is added because in case linked list is empty like l = [] here head = none or l = [0] head.next = none 
            return

        # Step 1: Push all nodes onto a stack
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        
        # Step 2: Reorder the list in-place
        length = len(stack)
        current = head
        for i in range(length // 2):
            # Pop a node from the stack (from the end)
            node_from_end = stack.pop()

            # Save the next node in the original order
            next_node = current.next

            # Insert the node from the end after the current node
            current.next = node_from_end
            node_from_end.next = next_node

            # Move the current pointer forward
            current = next_node

        # Step 3: Set the last node's next to None to end the list
        current.next = None