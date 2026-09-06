class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        output = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
    
        while top < bottom and left < right:
            for i in range(right - left):
                output.append(matrix[top][left + i])
            for i in range(bottom - top):
                output.append(matrix[top + i][right])
            for i in range(right - left):
                output.append(matrix[bottom][right - i])
            for i in range(bottom - top):
                output.append(matrix[bottom - i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
    
        # leftover strip: either a single row, a single column, or nothing
        if top == bottom:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
        elif left == right:
            for i in range(top, bottom + 1):
                output.append(matrix[i][left])
    
        return output
 