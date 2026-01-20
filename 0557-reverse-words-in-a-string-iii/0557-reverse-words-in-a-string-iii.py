class Solution(object):
    def reverseWords(self, s):
        x = split(s)
        z=[]
        for i in x:
            z.append(i[::-1])

        a=[]    
        for j in z:
            a.append(j+" ") 

        b="".join(a)
        c= b.strip()   
        return c   
        """
        :type s: str
        :rtype: str
        """
        