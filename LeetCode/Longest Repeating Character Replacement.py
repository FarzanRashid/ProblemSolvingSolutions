from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        left = 0
        max_freq = 0
        output = 0
        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])
            if (right - left + 1) - max_freq > k:
                if window[s[left]] == 1:
                    del window[s[left]]
                else:
                    window[s[left]] -= 1
                left += 1
            output = right - left + 1
        return output

# Time complexity = O(n) where n is the length of s
# Space complexity = O(k) where k is the size of the window
