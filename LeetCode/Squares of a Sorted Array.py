class Solution:
    def sortedSquares(self, nums):
        result = [1] * len(nums)
        left, right, pos = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result


# Time complexity = O(N)
# Space complexity = O(N)
