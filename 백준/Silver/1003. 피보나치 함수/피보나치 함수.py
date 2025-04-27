N = int(input())

dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    zero_cnt = dp[i-1][0] + dp[i-2][0]
    one_cnt = dp[i-1][1] + dp[i-2][1]
    dp[i] = (zero_cnt, one_cnt)

results = []

for _ in range(N):
    n = int(input())
    results.append(dp[n])

for zero, one in results:
    print(zero, one)

# N = int(input())

# def fibonacci(n):
#     if n == 0:
#         cnt[0] += 1
#         return 0
#     elif n == 1:
#         cnt[1] += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# results = []

# for _ in range(N):
#     n = int(input())
#     cnt = [0, 0]

#     fibonacci(n)
#     results.append((cnt[0], cnt[1]))
    
# for i, j in results:
#     print(i, j)