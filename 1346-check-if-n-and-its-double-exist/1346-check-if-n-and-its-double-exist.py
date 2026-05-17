class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # for i in range(len(arr)):
        #     a = i+1
        #     for j in range(a,len(arr))
        #         if i != j:
        #             print('hello')

        i = 0
        while  i < len(arr):

            j=i+1
            while j < len(arr):

                if i != j and i >= 0 and arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i] :
                    return True

                j += 1

            i +=1 
        return False   
        