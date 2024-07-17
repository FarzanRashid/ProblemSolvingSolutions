# Problem no - 868

# Time complexity O(n) where is the number bits required for input number
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        gap = 0
        last_bit = None
        while n:
            current_bit = n & 1
            if current_bit and last_bit is None:
                last_bit = current_bit
            elif current_bit:
                gap += 1
                if gap > result:
                    result = gap
                gap = 0
            elif not current_bit and last_bit:
                gap += 1
            n = n >> 1
        return result
