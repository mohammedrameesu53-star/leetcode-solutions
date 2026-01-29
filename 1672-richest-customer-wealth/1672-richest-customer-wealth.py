class Solution(object):
    def maximumWealth(self, accounts):
        arr=[]
        for i in accounts:
            a=0
            for j in i:
                a += j
            arr.append(a)

        sortedArr = sorted(arr)
        return sortedArr[-1]        
                


        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        