class Solution:
    def getDecimalValue(self, head) -> int:
        num_in_bin = ""
        while head:
            num_in_bin += str(head.val)
            head = head.next
        return int(num_in_bin, 2)
