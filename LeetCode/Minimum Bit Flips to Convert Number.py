# Problem no - 2220

# Time complexity O(1), the loop iterates a constant 32 times

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        diff = start ^ goal
        result = 0
        for bit_id in range(32):
            val = 1 << bit_id
            diff_bit = diff & val
            start_bit = start & val
            if diff_bit and start_bit:
                result += 1
            elif diff_bit and not start_bit:
                result += 1
        return result
