class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

# Time complexity = O(n) where n is the length of
 # Space complexity = O(n)