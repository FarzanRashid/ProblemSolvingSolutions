import math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            curr_weight = 0
            day = 1
            for weight in weights:
                if weight + curr_weight > mid:
                    day += 1
                    curr_weight = 0
                curr_weight += weight
            if day > days:
                l = mid + 1
            else:
                r = mid
        return l


# Time complexity = O(nlogm) where n is the number of weights and m is the sum of weights
# Space complexity = O(1)
