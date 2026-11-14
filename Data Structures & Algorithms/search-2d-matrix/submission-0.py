class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first = 0
        last = len(matrix) - 1


        while first <= last:
            mid = ((last - first) // 2) + first

            if target < matrix[mid][0]:

                last = mid - 1
            elif target > matrix[mid][-1]:

                first = mid + 1
            else:

                inner_first = 0
                inner_last = len(matrix[mid]) - 1

                while inner_first <= inner_last:
                    inner_mid = ((inner_last - inner_first) // 2) + inner_first

                    if matrix[mid][inner_mid] == target:
                        return True
                    elif matrix[mid][inner_mid] > target:
                        inner_last = inner_mid - 1
                    else:
                        inner_first = inner_mid + 1

                return False

        return False