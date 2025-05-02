class Solution:
    def rotate_in_place(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat) # row
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for i in range(n):
            l ,r = 0, n-1
            while l < r:
                mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
                l +=1
                r -=1
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate_in_place(mat)
        return False

    