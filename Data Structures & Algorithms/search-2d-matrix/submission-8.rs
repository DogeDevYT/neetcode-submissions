impl Solution {
    /*
    PATTERN MATCH GO:

    Basically we just do 2 rounds of binary search:
    
    round 1:
    check for rows' first entry being less than target and rows' last entry being more than target

    round 2:
    do binary search on the induvidual row and find element
    */
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        //store m and n for later
        let m: i32 = matrix.len() as i32;
        let n: i32 = matrix[0].len() as i32;

        //do binary search but with rows in the matrix
        let mut l: i32 = 0;
        let mut r: i32 = m - 1;

        let mut row: i32 = -1;

        while l <= r 
        {
            let mid: i32 = (l + r) / 2;

            let first: i32 = matrix[mid as usize][0];
            let last: i32 = matrix[mid as usize][(n-1) as usize];

            if first > target 
            {
                r = mid - 1;
            } else if last < target 
            {
                l = mid + 1;
            } else if first == target || last == target 
            {
                return true;
            } else if first < target && last > target 
            {
                row = mid;
                break; //dont forget to break!
            }
        }

        //check validity check
        if row == -1 
        {
            return false; //this means we havn't found a valid row at all so we can assume false
        }

        //regular binary search with elements in the actual row itself
        l = 0;
        r = n - 1;

        while l <= r
        {
            let mid: i32 = (l + r) / 2;

            let gurt: i32 = matrix[row as usize][mid as usize];

            if gurt < target 
            {
                l = mid + 1;
            } else if gurt > target 
            {
                r = mid - 1;
            } else 
            {
                //target found
                return true;
            }
        }

        //if we get here this means our element doesn't exist in the row
        return false;
    }
}
