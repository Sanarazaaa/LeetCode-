class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = []
        for i in nums:
            squared = i * i 
            num.append(squared)
        num.sort()
        return num
