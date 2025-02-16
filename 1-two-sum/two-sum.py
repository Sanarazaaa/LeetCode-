class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # Loop through the list using indices
            for j in range(i + 1, len(nums)):  # Check pairs without repetition
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices of the two numbers
        return []  # Return an empty list if no solution is found
