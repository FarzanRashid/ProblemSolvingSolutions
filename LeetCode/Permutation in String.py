from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter()
        left = 0
        k = len(s1)
        for right in range(len(s2)):
            s2_counter[s2[right]] += 1
            if right - left + 1 > k:
                if s2_counter[s2[left]] == 1:
                    del s2_counter[s2[left]]
                else:
                    s2_counter[s2[left]] -= 1
                left += 1
            if s2_counter == s1_counter:
                return True
        return False

# Time complexity       O(n) where n is the length of s2
# Space complexity      O(k) where k is the length of s1 since we are using
