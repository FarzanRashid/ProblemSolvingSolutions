class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        low = 0
        high = len(nums) - 1
        found = None
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                found = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if found is not None:
            output[0] = self.lowest_index(nums, found, target)
            output[1] = self.high_index(nums, found, target)
            return output
        return output

    def lowest_index(self, nums, found, target):
        low = 0
        high = found
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def high_index(self, nums, found, target):
        low = found
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                low = mid + 1
            else:
                high = mid - 1
        return high

# Time complexity = O(logn)
# Space complexity = O(1)
