class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for i in path:
            if i:
                if i == "..":
                    if stack:
                        stack.pop()
                elif i == ".":
                    continue
                else:
                    stack.append(i)
        return "/" + "/".join(stack)

# Time complexity = O(n)
# Space complexity = O(n)
