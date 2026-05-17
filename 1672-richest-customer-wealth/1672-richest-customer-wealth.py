class Solution(object):
    def maximumWealth(self, accounts):
        arr=[]
        for i in accounts:
            c = 0
            for j in i:
                c += j
            arr.append(c)
            
        return max(arr)      
                


        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        