class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        output = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                output[idx] = (i - idx)
            stack.append(i)
        return output

# Time complexity = O(n)
# Space complexity = O(n)
