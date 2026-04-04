class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        result = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - result):
                    result = total
                if total > target:
                    right -= 1
                else:
                    left += 1
        return result

# Time complexity = O(N^2)
# Space complexity = O(1)
