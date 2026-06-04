class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows: {1:[1,2,3],2:[4,5]}
        # cols: {1:[1,4,5,7], 2:[2,9]}
        # groups: {(0,0):1,2,4,9,8}
        rows = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        cols = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        groups = {(0,0):[],(1,0):[],(2,0):[],(0,1):[],(1,1):[],(2,1):[],(0,2):[],(1,2):[],(2,2):[]}
        rows_len = 9
        cols_len = 9

        for r in range(rows_len):
            for c in range(cols_len):
                if board[r][c] =='.':
                    continue

                number = board[r][c]

                if number in rows[r] or number in cols[c] or number in groups[(r//3,c//3)]:
                    return False
                else:
                    rows[r].append(number)
                    cols[c].append(number)
                    groups[(r//3,c//3)].append(number)
        return True


        