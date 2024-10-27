class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            num1 = [*nums1, *nums2]
            length = len(num1) 
            num1.sort()
            if length % 2 == 0:
                return (num1[(length // 2) - 1] + num1[length // 2]) / 2 # i'll be using the square brackets if i want  to return a list # to access the elements, i need to use square brackets
            else:
                return num1[length // 2]

