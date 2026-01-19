class Solution(object):
    def singleNumber(self, nums):
        x = tuple(nums)
        a=[]
        for i in x:
            if x.count(i) == 1:
                a.append(i)
        return a        

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        