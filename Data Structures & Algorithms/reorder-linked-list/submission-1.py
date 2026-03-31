# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        curr1 = head
        while curr1 is not None:
            curr1 = curr1.next
            l+=1
        times = math.floor(l / 2)
        
        curr1 = head
        for _ in range(times):
            curr2 = curr1
            while curr2.next.next is not None:
                curr2 = curr2.next
            desired = curr2.next
            curr2.next = None
            desired.next = curr1.next
            curr1.next = desired
            curr1 = desired.next
