# Problem no - 191

# Time complexity O(1)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        while n:
            last_bit = n & 1
            if last_bit:
                output += 1
            n = n >> 1
        return output
