class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []  # This will store all rows of Pascal's Triangle
        for i in range(numRows):
            row = [1]  # Initialize each row with the first element as 1
            
            # Check if there are previous rows in pascals_triangle
            if pascals_triangle:
                last_row = pascals_triangle[-1]  # Access the last row
                
                # Use a loop to find the middle elements of the last row
                for j in range(len(last_row) - 1):
                    row.append(last_row[j] + last_row[j + 1])
                    
                row.append(1)  # End each row with 1
            
            # Append the row to pascals_triangle
            pascals_triangle.append(row)
        
        return pascals_triangle
