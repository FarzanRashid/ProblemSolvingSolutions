class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o','u'}
        max_length = 0
        for i in range(k):
            if s[i] in vowels:
                max_length += 1
        output = max_length
        for i in range(k, len(s)):
            if s[i] in vowels:
                max_length += 1
            if s[i - k ] in vowels:
                max_length -= 1
            output = max(output, max_length)
        return output

# Time complexity = O(N)
# Space complexity = O(1)
