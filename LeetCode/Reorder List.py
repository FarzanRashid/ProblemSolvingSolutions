# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        curr = head
        while prev:
            tmp1 = curr.next
            tmp2 = prev.next

            curr.next = prev
            prev.next = tmp1

            curr = tmp1
            prev = tmp2

# Time complexity = O(n) where n is the number of nodes in the linked list
# Space complexity = O(1)
