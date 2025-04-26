class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c_sum= 0
        result = []
        for i in nums:
            c_sum += i
            result.append(c_sum)
        return result
