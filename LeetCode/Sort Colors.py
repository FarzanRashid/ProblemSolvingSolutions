class Solution:
    def sortColors(self, nums) -> None:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != 0 and nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] == 0 and nums[right] != 0:
                right -= 1
                left += 1
            elif nums[left] == 0 and nums[right] == 0:
                left += 1
            else:
                right -= 1
        num_of_zero = 0
        for num in nums:
            if num is 0:
                num_of_zero += 1
        left = num_of_zero
        right = len(nums) - 1
        while left < right:
            if nums[left] != 1 and nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] == 1 and nums[right] != 1:
                right -= 1
                left += 1
            elif nums[left] == 1 and nums[right] == 1:
                left += 1
            else:
                right -= 1
        return nums

# Time complexity = O(N)
# Space complexity = O(1)
