# Problem no - 693

# Time complexity O(n) where n is the number of bits required for input n

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_bit = None
        while n:
            last_bit = n & 1
            if last_bit == prev_bit:
                return False
            prev_bit = last_bit
            n = n >> 1
        return True
