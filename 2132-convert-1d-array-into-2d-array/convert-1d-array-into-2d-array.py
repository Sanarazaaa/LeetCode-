# 1d list is a simple list. not a list inside a list
# 0-indexed means: First element is at index 0, second at index 1, third at index 2, etc.
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]: # the function will take 3 inupts
        result = []
        if m*n == len(original):
            for i in range(0,len(original),n): #i will go from 0 to len(original), jumping n steps at a time.
                result.append(original[i:i+n]) #just slicing
        return result


