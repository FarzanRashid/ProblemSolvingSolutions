# Problem no - 3158

# Time complexity O(n) where is length of input list

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        seen = set()
        twins = []
        output = 0
        for i in nums:
            if i in num_set and i not in seen:
                twins.append(i)
                seen.add(i)
            else:
                num_set.add(i)
        if twins:
            for i in twins:
                output ^= i
        return output
