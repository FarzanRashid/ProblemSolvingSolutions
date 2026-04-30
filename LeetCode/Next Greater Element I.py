class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}
        output = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                num = nums2[stack.pop()]
                nge[num] = nums2[i]
            stack.append(i)
        for i in stack:
            nge[nums2[i]] = -1
        for i in nums1:
            output.append(nge[i])
        return output

# Time complexity = O(n)
# Space complexity = O(n)
