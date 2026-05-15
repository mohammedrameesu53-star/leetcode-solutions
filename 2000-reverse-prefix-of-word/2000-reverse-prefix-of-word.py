class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
            
        index = 0
        for i in range(len(word)):
            if word[i] == ch:
               index = i
               break

        v1= word[:index+1]
        v2= word[index+1:] 
        ans = v1[::-1]+v2

        return ans
        



        
        