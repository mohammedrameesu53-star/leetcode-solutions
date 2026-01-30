class Solution(object):
    def countWords(self, words1, words2):
        a=0
        for i in words1:
            count1 = words1.count(i)
            count2 = words2.count(i)
            if count1 == 1 and count2 == 1:
                a += 1
        return a        

        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        