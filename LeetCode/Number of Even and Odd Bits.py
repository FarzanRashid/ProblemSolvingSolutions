# Problem no - 2595

# Time complexity O(n) where n is number of bits required for input n

def evenOddBit(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    even = 0
    odd = 0
    bit_id = 0
    while n:
        val = n & 1
        if val and bit_id % 2 == 0:
            even += 1
        elif val and bit_id % 2 == 1:
            odd += 1
        n = n >> 1
        bit_id += 1
    return [even, odd]
