class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        row_number = - 1
        # find the row where element could be
        while top <= bottom:
            mid = top + (bottom - top) // 2
            # check if the mid element is between mid row
            # or not
            left = matrix[mid][0]
            right = matrix[mid][len(matrix[mid]) - 1]

            if target >= left and target <= right:
                # target is between this
                left = 0
                right = len(matrix[mid]) - 1

                while left <= right:
                    mid_col = left + (right - left) // 2

                    if matrix[mid][mid_col] == target:
                        return True
                    
                    elif matrix[mid][mid_col] > target:
                        right = mid_col - 1

                    else:
                        left =  mid_col + 1
                    
                return False

            
            elif target < left:
                bottom = mid - 1
            
            else:
                top = mid + 1

        return False
        