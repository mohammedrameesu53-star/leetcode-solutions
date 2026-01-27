class Solution(object):
    def reverseVowels(self, s):
        z = list(s)
        index =[]
        sounds =[]
        vowels ="aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                sounds.append(s[i])

        reversedSounds = sounds[::-1]
       
        for x in range(len(index)):
            z[index[x]] = reversedSounds[x]

        return "".join(z)    
                





        """
        :type s: str
        :rtype: str
        """
        