class Solution:
    def getIntersectionNode(self, headA, headB):
        vals = set()
        val = headA
        while val:
            vals.add(val)
            val = val.next
        val = headB
        while val:
            if val in vals:
                return val
            val = val.next
        return None
