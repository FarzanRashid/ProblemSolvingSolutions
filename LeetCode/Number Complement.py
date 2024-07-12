# Problem no - 476

# Time Complexity O(log n)

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = ""

        while num:
            last_bit = num & 1
            if last_bit:
                output += "0"
            else:
                output += "1"
            num = num >> 1
        return int(output[::-1], 2)
