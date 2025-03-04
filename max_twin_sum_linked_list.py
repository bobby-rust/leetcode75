from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head and not head.next:
            return 0

        cur_sum = 0
        max_sum = 0
        slow = head
        fast = head.next
        stack = []
        stack.append(slow.val)
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)

        slow = slow.next
        while slow:
            cur_sum = slow.val + stack.pop()
            max_sum = max(max_sum, cur_sum)
            slow = slow.next

        return max_sum
