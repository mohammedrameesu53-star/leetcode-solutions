class Solution(object):
    def plusOne(self, digits):
        n1 = []
        for i in digits:
            n1.append(str(i))
        n2 = "".join(n1)
        n3 =str(int(n2) + 1) 
        n4 =[]
        for i in n3:
            n4.append(int(i))
        return n4    
      
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        