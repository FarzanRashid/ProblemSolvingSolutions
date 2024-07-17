# Problem no- 2980

# Time complexity O(n ^ 2) where n is the length of input list

class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num = nums[i] | nums[j]
                last_bit = num & 1
                if not last_bit:
                    return True
        return False
