class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in letters:
            if i not in sentence:
                return False



        return True       


