# Problem no - 476

# Time Complexity O(n) where n is the number of bits required for num"

class Solution(object):
    def findComplement(self, num):
        if num == 0:
            return 1

        output = 0
        bit_id = 0

        while num:
            last_bit = num & 1
            if last_bit == 0:
                num = num | 1
                val = 1 << bit_id
                output = output | val

            num = num >> 1
            bit_id += 1
        return output
