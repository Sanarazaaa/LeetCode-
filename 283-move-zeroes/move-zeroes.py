class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeroes = []  # Initialize an empty list for non-zero elements
        
        # Loop through the original list and add non-zero elements to the new list
        for num in nums:
            if num != 0:
                non_zeroes.append(num)
        
        # Calculate the number of zeros to add
        zeros_to_add = len(nums) - len(non_zeroes)
        
        # Update nums in place with non-zeroes followed by the calculated zeros
        nums[:] = non_zeroes + [0] * zeros_to_add
