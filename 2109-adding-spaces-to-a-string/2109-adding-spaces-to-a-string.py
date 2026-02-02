class Solution(object):
    def addSpaces(self, s, spaces):
        spaces.append(len(s))
        arr = list(s)
        new=[]
        a=0
        for i in spaces:
            new.append(s[a:i])
            if i != len(s):
                new.append(" ")
                a = i
        return "".join(new)          
           


        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        