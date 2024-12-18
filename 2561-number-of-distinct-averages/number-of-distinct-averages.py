class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        distinct_avg = set()
        while len(nums) >1:
            avg = (nums[0] + nums[-1])/2
            distinct_avg.add(avg)
            nums.pop(0)
            nums.pop(-1)
        return len(distinct_avg)