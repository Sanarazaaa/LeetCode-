# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# current: Points to the node with value 1 (the first node in the list).
# current.next: Points to the node with value 2 (the second node in the list).
# next_node: Is assigned the value of current.next, which is the node with value 2.
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorder the linked list in-place using a stack.
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: # this is added because in case linked list is empty like l = [] here head = none or l = [0] head.next = none 
            return

        # Step 1: Push all nodes onto a stack
        re_order = []
        stack = []
        current = head
        while current != None: # while current: (this is also correct) while current:: This condition will evaluate to True as long as current is not None. When you reach the end of the linked list, current will become None, causing the loop to exit.
            stack.append(current)
            current = current.next  # This expression points to the next node in the linked list from the current node. If the current node is the last node, current.next will be None, indicating that there are no more nodes in the list.
        
        # Step 2: Reorder the list in-place
        length = len(stack)
        current = head
        for i in range(length // 2):
            # Pop a node from the stack (from the end)
            node_from_end = stack.pop() # 5 will be popped

            # Save the next node in the original order
            next_node = current.next # 

            # Insert the node from the end after the current node
            current.next = node_from_end 
            node_from_end.next = next_node

            # Move the current pointer forward
            current = next_node

        # Step 3: Set the last node's next to None to end the list
        current.next = None