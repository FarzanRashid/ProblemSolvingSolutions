from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for i in word:
                chars[ord(i) - ord('a')] += 1
            seen[tuple(chars)].append(word)
        return [value for item, value in seen.items()]

# Time complexity = O(n * k)
# Space complexity = O(n * k)
