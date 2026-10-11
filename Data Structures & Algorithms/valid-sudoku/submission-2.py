class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = dict() #block number
        rows = dict()
        cols = dict()
        for i in range(len(board)):
            if rows.get(i) == None:
                rows[i] = list()   
            box = i // 3 * 3
            for j in range(len(board)):
                if cols.get(j) == None:
                    cols[j] = list()

                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])

                if j == 3:
                    box += 1
                elif j == 6:
                    box += 1

                if boxes.get(box) == None:
                    boxes[box] = list()                
                
                if board[i][j] != ".":
                    if board[i][j] in boxes[box]:
                        return False
                    boxes[box].append(board[i][j])

        return True
            