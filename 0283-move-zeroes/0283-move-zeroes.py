class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)
        return nums        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        