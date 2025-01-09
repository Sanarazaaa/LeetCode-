class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        
        negative_count = sum(1 for num in nums if num < 0)
        
        return -1 if negative_count % 2 != 0 else 1
