class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num == ".":
                    continue
                z = (x // 3) * 3 + (y // 3)
                if num in rows[x] or num in cols[y] or num in boxs[z]:
                    return False
                rows[x].add(num)
                cols[y].add(num)
                boxs[z].add(num)
        return True