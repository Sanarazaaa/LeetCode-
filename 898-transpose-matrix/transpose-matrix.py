class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for col in range(len(matrix[0])) : # To find out how many columns there are, i have to check the length of any row 
            new_row = []
            for row in matrix:
                new_row.append(row[col])
            transpose.append(new_row)
        return transpose