# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = node = ListNode()
        prev = None

        while head:
            prev = head
            head = head.next
            if head == dummy:
                return True
            prev.next = node
        return False