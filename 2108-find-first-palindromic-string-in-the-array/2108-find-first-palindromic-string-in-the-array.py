class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        v=""
        for i in words:
            if i == i[::-1] :
                v = i
                break

        if len(v) == 0:
            return ""
                    
        return v               