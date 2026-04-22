class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in s:
            if i != "#":
                s_stack.append(i)
            else:
                if s_stack:
                    s_stack.pop()
        for i in t:
            if i != "#":
                t_stack.append(i)
            else:
                if t_stack:
                    t_stack.pop()
        return s_stack == t_stack

# Time complexity = O(m + n)
# Space complexity = O(m + n)
