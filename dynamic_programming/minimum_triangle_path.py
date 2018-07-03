"""
Find the shortest path from top to bottom triangle. Each cell can only be
added to adjacent neighbors in proceeding row.
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3],
 [7,3,9,3,6]
"""


class Triangle:
    def minimumTotal(self, triangle):
        """
        DP solution with O(n) time and space. Update cell with min sum as we go down.
        The last row should contain the smallest path sum.
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return min(triangle[0])
        
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):

                # check previous rows' adjacent cells
                # and check whether we will hit boundary limits
                if col != 0:
                    left = triangle[row][col] + triangle[row-1][col-1]
                else:
                    left = None

                if col != len(triangle[row])-1:
                    right = triangle[row][col] + triangle[row-1][col]
                else:
                    right = None
                
                # update cell value
                if left is None:
                    triangle[row][col] = right
                elif right is None:
                    triangle[row][col] = left
                else:
                    # update current cell with lowest sum
                    triangle[row][col] = min(left, right)

        return(min(triangle[-1]))


triangle = [[2], [3, 4]]
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [   [-1],
              [3, 2],
            [-3, 1, -1]]
Triangle().minimumTotal(triangle)