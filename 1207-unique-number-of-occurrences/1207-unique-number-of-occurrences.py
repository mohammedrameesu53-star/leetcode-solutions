class Solution(object):
    def uniqueOccurrences(self, arr):
        each = set(arr)
        occurances =[]
        for i in each:
            occurances.append(arr.count(i))

        unique = set(occurances) 

        if len(unique) == len(occurances):
            return True
        else:
            return False       
        """
        :type arr: List[int]
        :rtype: bool
        """
        