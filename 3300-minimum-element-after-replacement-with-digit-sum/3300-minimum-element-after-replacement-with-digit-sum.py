class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        for i in nums:
            a = str(i)
            n=0
            for j in a:
                n += int(j)
            arr.append(n)

        return min(arr)        