from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        output = 0
        fruit_counter = Counter()
        for right in range(len(fruits)):
            fruit_counter[fruits[right]] += 1
            while len(fruit_counter) > 2:
                if fruit_counter[fruits[left]] == 1:
                    del fruit_counter[fruits[left]]
                else:
                    fruit_counter[fruits[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output

# Time complexity = O(n) where n is the length of fruits
# Space complexity = O(1) since the size of the counter is at most 3
