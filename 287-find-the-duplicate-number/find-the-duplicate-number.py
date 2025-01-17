class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()  # Sorting first for two-pointer method to work
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:  # Duplicate found
                return nums[l]
            l += 1
            r += 1

        return -1  # If no duplicate found 