class Solution(object):
    def canBeEqual(self, target, arr):
        a =[]
        for i in target:
            if target.count(i) == arr.count(i) and len(target) == len(arr):
                a.append(True)
            else:
                a.append(False) 
        if False in a:
            return False
        else:
            return True                   
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        