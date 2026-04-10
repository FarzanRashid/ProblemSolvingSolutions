class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        wind = set()
        for i in range(len(nums)):
            if nums[i] in wind:
                return True
            wind.add(nums[i])
            if i - left >= k:
                wind.remove(nums[left])
                left += 1
        return False

# Time complexity       O(n) where n is the length of nums
# Space complexity      O(k) since we are using a set to store at most k elements
