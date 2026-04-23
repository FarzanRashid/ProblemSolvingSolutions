class Solution:
    def simplifyPath(self, path: str) -> str:
        words = path.split("/")
        stack = []
        for i in words:
            if i == ".":
                continue
            elif i == "..":
                stack.pop() if stack else ""
            elif i:
                stack.append(i)
        output = "/".join(stack) if stack else ""
        return "/" + output

# Time complexity = O(n)
# Space complexity = O(n)
