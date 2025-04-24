class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        new = []
        for i in range(0,len(original),n):
            if len(original) == m*n:
                new.append(original[i:i+n])
 # i have to append the sliced one not the original one           new.append(original)  
            else:
                return []
        return new