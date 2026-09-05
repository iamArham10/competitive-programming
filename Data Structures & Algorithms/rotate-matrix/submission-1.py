class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start = 0
        end = len(matrix) - 1

        while (start < end):
            for i in range(end-start):
                temp = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]
                matrix[end-i][start] = matrix[end][end-i]
                matrix[end][end-i] = matrix[start+i][end]
                matrix[start+i][end] = temp

            start += 1
            end -= 1
 