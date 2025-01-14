from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 针对 [[]] 这种情况，要特判
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        left = 0
        # 这里一定要记得减 1
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    # target = 3
    #
    # solution = Solution()
    # result = solution.searchMatrix(matrix, target)
    # print(result)

    matrix = [
        [1]
    ]

    solution = Solution()
    result = solution.searchMatrix(matrix, 2)
    print(result)
