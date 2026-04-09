class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        summation = sum(nums[:k])
        max_avg = summation / k
        for i in range(k, len(nums)):
            summation += nums[i]
            summation -= nums[i - k]
            max_avg = max(max_avg, summation / k)
        return max_avg

# Time complexity = O(N)
# Space complexity = O(1)
