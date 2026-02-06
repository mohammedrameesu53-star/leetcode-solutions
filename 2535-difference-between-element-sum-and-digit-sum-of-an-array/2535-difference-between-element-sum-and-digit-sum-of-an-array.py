class Solution(object):
    def differenceOfSum(self, nums):
        eleSum = 0
        for i in nums:
            eleSum += i
        digSum=0
        for j in nums:
            for k in str(j):
                digSum += int(k)  
        return abs(eleSum-digSum)          
        """
        :type nums: List[int]
        :rtype: int
        """
        