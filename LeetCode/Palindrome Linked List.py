# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode()
        vals = []
        dummy.next = head
        current = dummy
        while current.next:
            vals.append(current.next.val)
            current = current.next
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        for i in vals:
            if i != previous.val:
                return False
            previous = previous.next
        return True
