import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(float(pile) / mid)
            if hour <= h:
                r =  mid
            else:
                l = mid + 1
        return l

# Time complexity = O(nlogm) where n is the number of piles and m is the maximum pile size
# Space complexity = O(1)
