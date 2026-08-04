# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            curr = curr.next
        
        if curr is None:
            return head.next

        delayed = head
        while curr.next:
            curr = curr.next
            delayed = delayed.next
        
        delayed.next = delayed.next.next
        return head