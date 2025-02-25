class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to hold the rows
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            # Place the character in the appropriate row
            rows[current_row] += char
            
            # Decide whether to go up or down
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final zigzag string
        return ''.join(rows)
