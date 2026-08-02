import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x, y)
            if y > x:
                heapq.heappush(stones, x - y)
        return stones[0] * -1 if stones else 0

# Time complexity =  O(n log n) where n is the number of stones
# Space complexity = O(n) where n is the number of stones
