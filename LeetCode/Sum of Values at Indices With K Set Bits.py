# Problem no - 2859

# Time complexity O(n) where n is the length of input list

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        for i in range(len(nums)):
            x = i
            bits = 0
            for y in range(32):
                last_bit = x & 1
                if last_bit:
                    bits += 1
                x = x >> 1
            if bits == k:
                output += nums[i]
        return output
