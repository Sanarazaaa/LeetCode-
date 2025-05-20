#zero-indexed array means: Zero-based array indexing is a way of numbering the items in an array such that the first item of it has an index of 0

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            if  nums[i] < pivot:
                result.append(nums[i])
        for i in range(n):
            if  nums[i] == pivot:
                result.append(nums[i])
        for i in range(n):
            if  nums[i] > pivot:
                result.append(nums[i]) # (nums[i]) ---> here i is the index that's why we used square brackets
        return result
        
