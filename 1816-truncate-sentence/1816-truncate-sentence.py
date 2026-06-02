class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split()
        arr2 = arr[:k] 
        return " ".join(arr2)