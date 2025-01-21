class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        k = k % len(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums