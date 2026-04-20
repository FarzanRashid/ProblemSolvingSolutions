class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output

# Time complexity = O(n) where n is the length of nums
# Space complexity = O(1) since we are using the output array to store the results
