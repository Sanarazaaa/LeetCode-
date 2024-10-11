class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        t = []
        for i in nums:
            squared = i ** 2 # -4*-4 = 16, -1*-1 = 1 
            t.append(squared) # 16 will go to t, 
            t.sort()
        return t
