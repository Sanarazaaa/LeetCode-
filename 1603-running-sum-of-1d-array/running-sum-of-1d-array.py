class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num = [0] *len(nums) # this will give me [0,0,0,0]. this is used to create  alist of zeros
        num[0] = nums[0] # this will give me [1]
        for i in range(1,len(nums)):
            num[i] = nums[i] + num [i-1]
        return num
