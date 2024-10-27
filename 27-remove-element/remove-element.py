# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         num = []
#         pos = 0
#         for i, j in enumerate(nums): # i is the index, but j is the element itself
#             if j != val:
#                 num.append(j) 
#         return len(nums)
# This was the error that i was getting. TypeError: ([2, 2], 2) is not valid value for the expected return type integer[]. also, i need to return an integer that have the new length of the modified nums list (the nums should be modified in-place to contain elements that arent equal to val)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0  # Initialize the pointer for the new position
        for num in nums:
            if num != val:
                nums[pos] = num  # Place non-val element at the `pos` index
                pos += 1  # Move the pointer to the next position
        return pos  # Return the length of the modified list
