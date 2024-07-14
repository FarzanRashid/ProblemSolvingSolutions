# Problem no - 1356

# Time complexity O (n log n) where n is the size of the input list

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output = []
        bits_dict = {}
        for i in arr:
            bits = 0
            x = i
            while x:
                last_bit = x & 1
                if last_bit:
                    bits += 1
                x = x >> 1
            if bits in bits_dict:
                bits_dict[bits].append(i)
            else:
                bits_dict[bits] = [i]
        for i in range(16):
            if i in bits_dict:
                output += sorted(bits_dict[i])
        return output
