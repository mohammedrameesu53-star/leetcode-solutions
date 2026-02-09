class Solution(object):
    def sumDivisibleByK(self, nums, k):
        unique = set(nums)
        sum=0
        for i in unique:
            if nums.count(i) % k == 0 :
                sum += i * nums.count(i)
        return sum        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        