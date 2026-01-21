class Solution(object):
    def sortArrayByParity(self, nums):
        nums1 =nums
        nums2 =[]
        for i in nums1:
            if i % 2 == 0:
                nums2.append(i)
        for i in nums1:
            if not i % 2 == 0:
                nums2.append(i)
        return nums2                 
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        