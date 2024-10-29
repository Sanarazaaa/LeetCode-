class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroes = []  # Initialize an empty list for non-zero elements
        ones_count = 0  # Counter for 1s
        twos_count = 0  # Counter for 2s

        for num in nums:
            if num == 0:
                zeroes.append(num)
            elif num == 1:
                ones_count += 1
            elif num == 2:
                twos_count += 1
        
        nums[:] = zeroes + [1] * ones_count + [2] * twos_count

# wrong approach as this will not work if there are fewer than 1 and 2 
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         zeroes = []  # Initialize an empty list for zero elements
        
#         # Loop through the original list and count zeros, ones, and twos
#         for num in nums:
#             if num == 0:
#                 zeroes.append(num)
        
#         # Calculate the number of zeros to add
#         non_zeroes = len(nums) - len(zeroes)  # Count of non-zero elements
        
#         # Here, you're multiplying non_zeroes by 2 to get twice the number of 1s and 2s
#         nums[:] = zeroes + [1] * (non_zeroes // 2) + [2] * (non_zeroes // 2)
