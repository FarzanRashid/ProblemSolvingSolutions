class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        output = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            output = max(output, right + 1 - left)
        return output

# Time complexity       O(n) where n is the length of s
# Space complexity      O(k) where k is the size of the longest substring without repeating characters
