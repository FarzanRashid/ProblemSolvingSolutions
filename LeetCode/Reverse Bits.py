# Problem no - 190
class Solution:
    # @param n, an integer
    # @return an integer

    # Time Complexity O(1)
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            shifted_val = n >> i
            ith_index = shifted_val & 1
            target_index = 31 - i
            if ith_index:
                val = 1 << target_index
                result = result | val
            else:
                val = 1 << target_index
                val = ~val
                result = result & val
        return result
