class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # Get the length of the list
        max_value = nums[0]  # Initialize the max_value variable  
        for i in range(0, n): # Find the maximum value in the list
            if max_value < nums[i]:
                max_value = nums[i]
        return nums.index(max_value)  # Return the index of the maximum value
