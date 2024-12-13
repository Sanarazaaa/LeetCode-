class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])  # Find number of rows and columns
        if m * n != r * c:
            return mat  # If reshaping isn't possible, return the original matrix
        
        # Flatten the original matrix into a single list
        flat_list = []
        for row in mat:
            for elem in row:
                flat_list.append(elem)
        
        # Reshape the flattened list into a new matrix with r rows and c columns
        reshaped_matrix = []
        for i in range(0, len(flat_list), c):
            reshaped_matrix.append(flat_list[i:i + c])
        
        return reshaped_matrix  # Return the reshaped matrix after the loop completes
