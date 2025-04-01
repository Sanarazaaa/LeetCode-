from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Initialize a list to count the occurrences of each number, assuming numbers range from 0 to 1000.
        # This means each index represents a number, and the value at that index represents its count.
        count = [0] * 1001
      
        # Loop through each list in the list of lists `nums`.
        for num_list in nums:
            # Using a set to avoid counting duplicates in the same list.
            unique_nums = set(num_list)
            # Increment the count for each number found in the list.
            for num in unique_nums:
                count[num] += 1
      
        # Return a list of numbers (index) where the count is equal to the length of `nums`
        # i.e., the number appeared in all lists.
        return [num for num, frequency in enumerate(count) if frequency == len(nums)]