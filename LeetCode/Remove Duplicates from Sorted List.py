class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        elif head.next is None:
            return head
        elif head.val == head.next.val:
            head.next = self.find_next_value(head)
        self.deleteDuplicates(head.next)
        return head

    def find_next_value(self, node):
        current = node
        while current:
            if current.val != node.val:
                break
            current = current.next
        return current
