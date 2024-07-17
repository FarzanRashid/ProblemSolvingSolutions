# Problem no - 2917

# Time complexity O(n) where n is length of input list

class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # bit_index = {}
        # bit_index_flip = set()
        # output = []
        # for i in nums:
        #     bit_id = 0
        #     x = i
        #     for y in range(32):
        #         last_bit = x & 1
        #         if last_bit:
        #             bit_index[bit_id] = bit_index.get(bit_id, 0) + 1
        #         bit_id += 1
        #         x = x >> 1
        # for key in bit_index:
        #     if bit_index[key] >= k:
        #         bit_index_flip.add(key)
        # for i in range(32):
        #     if i in bit_index_flip:
        #         output.append("1")
        #     else:
        #         output.append("0")
        # return int("".join(output[::-1]), 2)
        result = 0
        for bit_id in range(32):
            count = 0
            for num in nums:
                if count == k:
                    break
                bit_val = 1 << bit_id
                val = num & bit_val
                if val:
                    count += 1
            if count == k:
                bit_val = 1 << bit_id
                result = result | bit_val
        return result
