/*
Ok we can get around this problem by keeping hash sets of cols, pos_diagonals (r + c), and neg diagonals (r - c),
and just iterating through all the possible combinations
*/
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        let mut col = vec![false; n];
        let mut pos_diag = vec![false; 2 * n];
        let mut neg_diag = vec![false; 2 * n];
        let mut res = Vec::new();
        let mut board = vec![vec!['.'; n]; n];

        Self::backtrack(0, n, &mut col, &mut pos_diag, &mut neg_diag, &mut board, &mut res);
        res
    }

    fn backtrack(
        r: usize, 
        n: usize,
        col: &mut Vec<bool>,
        pos_diag: &mut Vec<bool>,
        neg_diag: &mut Vec<bool>,
        board: &mut Vec<Vec<char>>,
        res: &mut Vec<Vec<String>>,
    ) 
    {
        if r == n 
        {
            let copy = board.iter().map(|row|
                row.iter().collect()).collect();
            res.push(copy);
            return;
        }

        for c in 0..n 
        {
            if col[c] || pos_diag[r + c] || neg_diag[r - c + n] 
            {
                continue;
            }

            col[c] = true;
            pos_diag[r + c] = true;
            neg_diag[r - c + n] = true;
            board[r][c] = 'Q';

            Self::backtrack(r + 1, n, col, pos_diag, neg_diag, board, res);

            col[c] = false;
            pos_diag[r + c] = false;
            neg_diag[r - c + n] = false;
            board[r][c] = '.';
        }
    }
}
