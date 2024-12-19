class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(set(nums), reverse=True) # Remove duplicates and sort in descending order
        if len(n) >= 3:
            return n[2]  
        else:
            return n[0]  
