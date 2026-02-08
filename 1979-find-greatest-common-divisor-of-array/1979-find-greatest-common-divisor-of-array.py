class Solution(object):
    def findGCD(self, nums):
        big=max(nums)
        small=min(nums)
        divisors_1=[]
        divisors_2=[]
        for i in range(1,small+1):
            if small%i == 0:
                divisors_1.append(i)
        for j in divisors_1:
            if big% j == 0:
                divisors_2.append(j)
        return max(divisors_2)        



        """
        :type nums: List[int]
        :rtype: int
        """
        