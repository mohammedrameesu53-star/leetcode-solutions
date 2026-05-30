class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr1=[]
        for i in range(m):
            arr1.append(nums1[i])
   
        arr2=[]
        for i in range(n):
            arr2.append(nums2[i])
        arr1.extend(arr2)
        arr1.sort()
        for i in range(len(arr1)):
            nums1[i] = arr1[i]
            
        return nums1    

             
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        