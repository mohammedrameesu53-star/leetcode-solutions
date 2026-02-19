class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        for j in range(len(nums)):        
            if nums[j] < target:
                pass
            else:
                return j    

        if nums[-1] < target:
            return len(nums)





        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        