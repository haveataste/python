def solveSudoku(board: list) -> None:
    def flip(i: int, j: int, digit: int):
        line[i] ^= (1 << digit)
        column[j] ^= (1 << digit)
        block[i // 3][j // 3] ^= (1 << digit)

    def dfs(pos: int):
        nonlocal valid
        if pos == len(spaces):
            valid = True
            return

        i, j = spaces[pos]
        mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
        while mask:
            digitMask = mask & (-mask)
            digit = bin(digitMask).count("0") - 1
            flip(i, j, digit)
            board[i][j] = str(digit + 1)
            dfs(pos + 1)
            flip(i, j, digit)
            mask &= (mask - 1)
            if valid:
                return

    line = [0] * 9
    column = [0] * 9
    block = [[0] * 3 for _ in range(3)]
    valid = False
    spaces = list()

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                digit = int(board[i][j]) - 1
                flip(i, j, digit)

    while True:
        modified = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    mask = ~(line[i] | column[j] |
                             block[i // 3][j // 3]) & 0x1ff
                    if not (mask & (mask - 1)):
                        digit = bin(mask).count("0") - 1
                        flip(i, j, digit)
                        board[i][j] = str(digit + 1)
                        modified = True
        if not modified:
            break

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                spaces.append((i, j))

    dfs(0)