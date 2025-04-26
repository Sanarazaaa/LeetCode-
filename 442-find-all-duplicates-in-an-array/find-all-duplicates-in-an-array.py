class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            index = abs(i)-1
            if nums[index]>0:
                nums[index] = -nums[index]
            else:
                result.append(abs(i))
        return result
