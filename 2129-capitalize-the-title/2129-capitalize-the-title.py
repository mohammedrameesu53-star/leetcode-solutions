class Solution(object):
    def capitalizeTitle(self, title):
        lowerTitle = title.lower()
        arr = lowerTitle.split(" ")
        corrected = []
        for i in arr:
            if len(i) <= 2:
                corrected.append(i)
            else: 
                word = list(i)
                word[0] = word[0].upper()
                ans = "".join(word)
                corrected.append(ans)

           
        return " ".join(corrected)    

        """
        :type title: str
        :rtype: str
        """
       