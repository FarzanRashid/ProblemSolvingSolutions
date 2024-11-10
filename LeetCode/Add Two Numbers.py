class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        head = ListNode()
        current = head
        remainder = 0
        while l1 and l2:
            add = l1.val + l2.val + remainder
            if add >= 10:
                remainder = add // 10
                add = add % 10
            else:
                remainder = 0
            node = ListNode(add)
            current.next = node
            current = node
            l1 = l1.next
            l2 = l2.next
        while l1:
            add = l1.val + remainder
            if add >= 10:
                remainder = add // 10
                add = add % 10
            else:
                remainder = 0
            node = ListNode(add)
            current.next = node
            current = node
            l1 = l1.next
        while l2:
            add = l2.val + remainder
            if add >= 10:
                remainder = add // 10
                add = add % 10
            else:
                remainder = 0
            node = ListNode(add)
            current.next = node
            current = node
            l2 = l2.next
        if remainder:
            node = ListNode(remainder)
            current.next = node
        return head.next
