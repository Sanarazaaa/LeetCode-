class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        total = 0
        for value in count_dict.values():
            if value >= 2:
                n1 = value*(value-1)//2 # if there is a value that appears more than 2 times, only then we can make good pairs
                total += value * (value - 1) // 2
        return total
