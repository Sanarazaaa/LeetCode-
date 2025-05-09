# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: # if there is no head and there is no head.next then return None
            return None
        slow = head 
        fast = head.next.next if head.next else None # why fast = head.next.next? well, we have to start head.next.next first so that slow can reach to a point that is one less than the middle
        while fast and fast.next: # in case there is still a value in fast and fast.next
            slow = slow.next # move slow pointer with one pointer
            fast = fast.next.next # move fast pointer with two
        slow.next = slow.next.next # when you reach at the point before the middle point then connect it with the node after middle one. why are we stopping before middle one? so that the link isnt lost.
        return head