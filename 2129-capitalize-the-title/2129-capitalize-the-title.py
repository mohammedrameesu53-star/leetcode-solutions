class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        t1 = title.lower().split(" ")
        res=[]
        for i in t1:
            if len(i)>2:
                res.append(i.title())
            else:
                res.append(i)
        return " ".join(res)