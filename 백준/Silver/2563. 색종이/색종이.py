paper = [[0] * 100 for _ in range(100)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
area = 0
for row in paper:
    area += sum(row)
print(area)