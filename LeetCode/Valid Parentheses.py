class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {")": "(", "}":"{", ']': '['}
        stack = []
        for i in s:
            if i in closing_brackets:
                if not stack or closing_brackets[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return not stack

# Time complexity = O(n) where n is the length of s
# Space complexity = O(n) in the worst case when all characters are opening brackets
