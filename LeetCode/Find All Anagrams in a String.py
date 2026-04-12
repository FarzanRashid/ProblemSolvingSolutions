from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = Counter()
        left = 0
        k = len(p)
        output = []
        for right in range(len(s)):
            s_counter[s[right]] += 1
            if right - left + 1 > k:
                if s_counter[s[left]] == 1:
                    del s_counter[s[left]]
                else:
                    s_counter[s[left]] -= 1
                left += 1
            if s_counter == p_counter:
                output.append(left)
        return output

# Time complexity       O(n) where n is the length of
# Space complexity      O(k) where k is the length of p