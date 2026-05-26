class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        arr1= s.split()
        print(arr1)
        arr2 = arr1[::]
        for i in arr1:
            for a in i:
                if a not in letters:
                    del arr2[int(a)-1]
                    string = list(i[::])
                    string.remove(a)
                    value = "".join(string)
                    arr2.insert(int(a)-1,value)
            

        return " ".join(arr2)