class Solution(object):
    def findKthLargest(self, nums, k):
        ordered = sorted(nums)
        return ordered[-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        