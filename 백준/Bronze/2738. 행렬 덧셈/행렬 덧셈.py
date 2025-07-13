N, M = map(int, input().split())
result =[]
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    row=[]
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:
    print(*row)