# Problem no - 1486

# Time complexity O(n) where n is the input n

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        result = 0
        for i in range(n):
            nums.append(start + 2 * i)
        for i in nums:
            result ^= i
        return result
