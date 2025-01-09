class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if math.prod(nums) >= 1:
            return 1
        elif math.prod(nums) <= -1:
            return -1
        elif math.prod(nums) ==0:
            return 0
