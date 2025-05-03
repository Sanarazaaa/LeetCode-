class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            l = 0
            r = len(nums)-1
            first_pos = -1
            while l <= r: #comparision sign and then equals to
                mid = (l+r)//2
                if nums[mid]==target:
                    first_pos = mid
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return first_pos
        def findLast(nums, target):
                l = 0
                r = len(nums)-1
                last_pos = -1
                while l <= r: #comparision sign and then equals to
                    mid = (l+r)//2
                    if nums[mid] == target:
                        last_pos = mid
                        l = mid+1
                    elif nums[mid] <= target:
                        l = mid+1
                    else:
                        r = mid-1
                return last_pos
        first = findFirst(nums,target)
        if first == -1:
            return [-1,-1]
        last = findLast(nums, target)
        return [first,last]



