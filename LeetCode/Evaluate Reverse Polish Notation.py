import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": operator.add, "/": operator.truediv, "*": operator.mul, "-": operator.sub}
        stack = []
        for i in tokens:
            if i in ops:
                first_num = stack.pop()
                second_num = stack.pop()
                num = int(ops[i](second_num, first_num))
                stack.append(num)
            else:
                stack.append(int(i))
        return int(stack[-1])

# Time complexity = O(n)
# Space complexity = O(n)
