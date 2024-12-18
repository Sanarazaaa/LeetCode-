class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)  # Length of the array
        for i in range(n + 1):  # Check from 0 to n
            if i not in nums:  # If `i` is missing, return it
                return i
