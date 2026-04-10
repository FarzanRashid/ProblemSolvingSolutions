class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = blocks[:k].count("W")
        min_count = w_count
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                w_count += 1
            if blocks[i-k] == "W":
                w_count -= 1
            min_count = min(min_count, w_count)
        return min_count

# Time complexity       O(n) where n is the length of blocks
# Space complexity      O(1) since we are using a constant amount of space
