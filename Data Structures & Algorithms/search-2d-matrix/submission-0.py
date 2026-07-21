class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target < i[-1]:
                for n in i:
                    if target == n:
                        return True
            elif target == i[-1]:
                return True
            else:
                continue
        return False
