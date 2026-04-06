class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(left + 1, right, s) or self.is_palindrome(left, right - 1,
                                                                                    s)
            left += 1
            right -= 1
        return True

    def is_palindrome(self, l, r, chars):
        while l < r:
            if chars[l] != chars[r]:
                return False
            l += 1
            r -= 1
        return True

# Time complexity = O(N)
# Space complexity = O(1)
