'''
https://leetcode.com/problems/search-a-2d-matrix/
'''
class Solution(object):
    def searchMatrixUnSorted(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        T ~ mlog(n)
        """
        for item in matrix:
            left, right = 0, len(item)-1
            mid = (left+right)//2
            while left <= right:
                if target==item[mid]:
                    return True
                elif target<item[mid]:
                    right=mid-1
                elif target>item[mid]:
                    left=mid+1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        T ~ log(m*n)
        """
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        if not (top <= bot):
            return False
        mid = (top + bot) // 2
        l, r = 0, rows - 1
        while l<=r:
            m = (l + r) // 2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True

        return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
s = Solution()
print(s.searchMatrix(matrix, target=3))