class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        output = [1] * len(prices)
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                output[idx] = prices[idx] - prices[i]
            stack.append(i)
        while stack:
            idx = stack.pop()
            output[idx] = prices[idx]

        return output

# Time complexity = O(n) where n is the length of prices
# Space complexity = O(n)
