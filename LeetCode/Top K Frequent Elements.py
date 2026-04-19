from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        heap = []
        for num, freq in num_freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]

# Time complexity = O(n log k)
# Space complexity = O(n)
