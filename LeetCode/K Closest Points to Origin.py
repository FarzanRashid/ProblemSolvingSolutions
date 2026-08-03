from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (dist * -1, x, y))
            while len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for z, x, y in heap]

# Time Complexity: O(n log k)
# Space Complexity: O(k)
