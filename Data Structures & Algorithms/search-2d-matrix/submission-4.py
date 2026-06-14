class Solution:
    """
    PATTERN MATCH GO:

    Basically we just do 2 rounds of binary search:
    
    round 1:
    check for rows' first entry being less than target and rows' last entry being more than target

    round 2:
    do binary search on the induvidual row and find element
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #store m and n into variables for easy lookup later
        m = len(matrix)
        n = len(matrix[0])

        #binary search on rows as described above
        l, r = 0, m - 1

        row = -1

        while row == -1 and l <= r:
            mid = (l + r) // 2

            first = matrix[mid][0]
            last = matrix[mid][n-1]

            if last < target:
                l = mid + 1
            elif first > target:
                r = mid - 1
            elif (first < target and last > target):
                row = mid
                break
            elif first == target or last == target:
                return True
        
        if row == -1:
            return False #if we can't even find our target row we can exit quickly
        
        #now we can do our basic binary search on the row itself

        #reset our left and right pointrs
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2

            gurt = matrix[row][mid]

            if gurt < target:
                l = mid + 1
            elif gurt > target:
                r = mid - 1
            elif gurt == target:
                return True
        
        #return False since we've binary searched everything so we can just return False
        return False