class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count >= 2:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            count = max(count, right - left)
        return count

# Time complexity = O(n) where n is the length of nums
# Space complexity = O(1)
