from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        need = len(t_freq)
        have = 0
        left = 0
        res_len = float('inf')
        res_index = [0, 0]
        window = Counter()
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in t_freq and window[s[right]] == t_freq[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res_index = [left, right + 1]
                window[s[left]] -= 1
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1
        return s[res_index[0]: res_index[1]] if res_len != float('inf') else ""

# Time complexity = O(n) where n is the length of s
# Space complexity = O(k) where k is the length of t
