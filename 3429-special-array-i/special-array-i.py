# parity means odd or even. if the 
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pairs = []
        for i in range(len(nums)-1):
            pairs.append((nums[i], nums[i + 1]))
            for i in range(len(pairs)):
             if (pairs[i][0] % 2) == (pairs[i][1] % 2):
                return False
        return True
        