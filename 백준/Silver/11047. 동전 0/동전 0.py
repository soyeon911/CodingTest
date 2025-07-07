N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
for coin in reversed(coins):
    if K >= coin:
        cnt += K//coin
        K = K % coin

print(cnt)