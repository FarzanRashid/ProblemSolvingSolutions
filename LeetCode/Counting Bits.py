# Problem No - 338

# Time Complexity O(n log n)
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []

        for i in range(n + 1):
            sum_of_ones = 0
            while i:
                if i & 1:
                    sum_of_ones += 1
                i = i >> 1
            output.append(sum_of_ones)

        return output
