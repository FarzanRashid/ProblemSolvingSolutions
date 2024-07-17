# Problem no - 1720

# Time complexity O(n) where n is length of input list

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        output = [first]
        for i in range(len(encoded)):
            output.append(output[i] ^ encoded[i])

        return output
