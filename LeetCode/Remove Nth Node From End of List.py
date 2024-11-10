class Solution:
    def removeNthFromEnd(self, head, n: int) :
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        counter = 1
        result = None
        current = previous
        while current:
            if counter == n:
                current = current.next
                counter += 1
            else:
                next_node = current.next
                current.next = result
                result = current
                current = next_node
                counter += 1
        return result
