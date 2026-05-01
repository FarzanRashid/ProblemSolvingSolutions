class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        output = "".join(stack)
        output = output.lstrip("0")
        return output if output else '0'

# Time complexity = O(n)
# Space complexity = O(n)
