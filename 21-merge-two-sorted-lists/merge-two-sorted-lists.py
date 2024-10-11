# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()  # head of the linked list but doesn't represent a value in the output
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2  # Fixed node.next2 to node.next
                list2 = list2.next
            node = node.next
        
        node.next = list1 if list1 else list2
        
        return dummy.next  # We got nothing in dummy, but in dummy.next, we will get something
