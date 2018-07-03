"""
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

s = 'PAYPALISHIRING'
numRows = 3

class Zigzag:
    def convert(self, s, numRows):
        """
        Set a "direction" variable that moves up and down the rows. Populate characters
        in our answer matrix as we read string s left to right. Reverse directions if we
        reach top or bottom rows.
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows >= len(s)) or (numRows == 1):
            return s
        curr_row = 0
        direction = -1 # positive moves down, negative moves up
        matrix = [[''] for i in range(numRows)]
        for i in s:
            matrix[curr_row][0] += i
            if (curr_row == 0) or (curr_row == numRows-1):
                direction *= -1  # reverse directions
            curr_row += direction
        return(''.join(row[0] for row in matrix))
