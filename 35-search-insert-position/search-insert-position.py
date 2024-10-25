class Solution:
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums) # reason for adding this is in case one element is missing. for instance in case nums = [1,3,5,6] and target = 7
