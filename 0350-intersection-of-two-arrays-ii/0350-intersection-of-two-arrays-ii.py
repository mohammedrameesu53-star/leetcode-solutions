class Solution(object):
    def intersect(self, nums1, nums2):
        ans =[]
        for i in set(nums1):
          ans.extend([i] * min(nums1.count(i),nums2.count(i)))
        return ans  
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        