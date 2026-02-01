class Solution(object):
    def countPrefixes(self, words, s):
        a=0
        for i in words:
            if s.startswith(i):
                a+=1
        return a        

        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        