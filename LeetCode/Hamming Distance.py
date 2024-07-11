# Problem No - 463

# Time Complexity O(1)
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        val = x ^ y

        for i in range(32):
            one = 1 << i
            if one & val:
                result += 1
        return result
