class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                ans += i
                count += 1
        if count == 0:
            return 0        
        avg = ans / count 
        return math.floor(avg)      