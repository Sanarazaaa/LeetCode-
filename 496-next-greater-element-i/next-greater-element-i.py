class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in nums1:
            if i in nums2:
                pos = nums2.index(i)  # Find the position of i in nums2
                greater_found = -1   # Default to -1 if no greater element is found
                for j in nums2[pos + 1:]:  # Check elements after i in nums2
                    if j > i:
                        greater_found = j
                        break  # Exit the loop once the next greater element is found
                stack.append(greater_found)  # Append the result (greater element or -1)
            else:
                stack.append(-1)  # Append -1 if i is not in nums2
        return stack
