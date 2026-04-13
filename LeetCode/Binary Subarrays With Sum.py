class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
        return self.at_most(nums, goal) - self.at_most(nums, goal - 1)
    def at_most(self, nums, goal):
        if goal < 0:
            return 0
        left = 0
        summation = 0
        count = 0
        for right in range(len(nums)):
            summation += nums[right]
            while summation > goal:
                summation -= nums[left]
                left += 1
            count += right + 1 - left
        return count

# Time complexity = O(n) where n is the length of nums
# Space complexity = O(1)
