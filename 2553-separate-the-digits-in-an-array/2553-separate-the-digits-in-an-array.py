class Solution(object):
    def separateDigits(self, nums):
        arr=[]
        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    arr.append(int(j))
            else:
                arr.append(i)
        return arr                

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        