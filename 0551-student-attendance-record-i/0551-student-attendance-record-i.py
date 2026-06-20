class Solution:
    def checkRecord(self, s: str) -> bool:
        p = 0
        a = 0
        l = 0
        for i in s:
            if i == "P":
                p += 1
            if i == "A":
                a += 1
            if i == "L":
                l += 1

        if "LLL" in s:
            return False

        if a < 2 :
            return True
        else:
            return False             