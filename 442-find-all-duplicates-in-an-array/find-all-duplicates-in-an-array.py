class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        dup = []
        for num in nums:
            if num in unique:
                dup.append(num)
            else:
                unique.add(num)
        return dup
