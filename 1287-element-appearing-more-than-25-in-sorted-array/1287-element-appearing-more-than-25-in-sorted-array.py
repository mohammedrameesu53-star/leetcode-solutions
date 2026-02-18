class Solution(object):
    def findSpecialInteger(self, arr):
        a=0
        for i in arr:
            if arr.count(i) > a:
                a = arr.count(i)
                ans = i
        return ans      
        """
        :type arr: List[int]
        :rtype: int
        """
        