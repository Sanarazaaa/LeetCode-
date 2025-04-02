class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = [0] * 1001
        for num_list in nums:
            unique_nums = set(num_list)
            for num in unique_nums:
                count[num] += 1
        return [num for num, frequency in enumerate(count) if frequency == len(nums)]