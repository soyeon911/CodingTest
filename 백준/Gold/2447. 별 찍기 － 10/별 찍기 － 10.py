N = int(input())

board = [[' ' for _ in range(N)] for _ in range(N)]
def pattern(x, y, size):
    if size == 1:
        board[x][y] = '*'
        return
    new_size = size // 3
    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue
            pattern(x + dx * new_size, y + dy * new_size, new_size)

pattern(0, 0, N)
for row in board:
    print(''.join(row))