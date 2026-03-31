class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a, z = 0, len(matrix) - 1
        l = len(matrix[0])

        if matrix[a][0] > target or matrix[z][l-1] < target:
            return False

        while a < z:
            mid = (a + z) // 2
            if matrix[mid][l-1] < target:
                a = mid + 1
            else:
                z = mid

        row = a
        s, f = 0, l - 1
        while s <= f:
            m = (s + f) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                f = m - 1
            else:
                s = m + 1

        return False