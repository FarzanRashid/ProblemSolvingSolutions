class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            l, r = 0, (len(matrix[mid])) - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] > target:
                    r = m - 1
                else:
                    l = m + 1
            if matrix[mid][m] > target:
                right = mid - 1
            else:
                left  = mid + 1
        return False

# Time complexity = O(logm×logn) where m is the number of rows and n is the number of columns
# Space complexity = O(1)
