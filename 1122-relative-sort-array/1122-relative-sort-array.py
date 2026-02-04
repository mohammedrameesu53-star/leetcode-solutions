class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans=[]
        other=[]
        for i in arr2:
            if i in arr1:
               count = arr1.count(i)
               ans.extend([i]*count)
        for j in arr1:
            if j not in arr2:
                other.append(j)       
        ans.extend(sorted(other)) 
        return ans        
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        