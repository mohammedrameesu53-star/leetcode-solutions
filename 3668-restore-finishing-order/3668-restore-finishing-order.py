class Solution(object):
    def recoverOrder(self, order, friends):
        arr=[]
        for i in order:
            if i in friends:
                arr.append(i)
        return arr        

        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        