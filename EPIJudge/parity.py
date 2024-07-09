# Time complexity O(n), n is the length of binary form of integer x.
def parity(x: int) -> int:
    num_of_ones = 0
    while x:
        if x & 1 and not num_of_ones:
            num_of_ones = not num_of_ones
        elif x & 1 and num_of_ones:
            num_of_ones = not num_of_ones
        x >>= 1
    return num_of_ones
