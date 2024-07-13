# Problem no - 1009

# Time Complexity O(n) where n is required bits for input n

class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        result = 0
        bit_id = 0
        while n:
            last_bit = n & 1
            if not last_bit:
                val = 1 << bit_id
                result = result | val
            bit_id += 1
            n = n >> 1
        return result
