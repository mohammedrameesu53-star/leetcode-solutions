class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        # if num[-1] == '0':
        #     del num[-1]
        arr = list(num[::-1])
        for i in range(len(arr)):
            if arr[i] != '0':
                index = i
                break

        new = arr[index:]        

        return "".join(new[::-1])           
              

            

