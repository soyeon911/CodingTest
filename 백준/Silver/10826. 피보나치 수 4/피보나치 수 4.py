N = int(input())

#0부터 N까지 피보나치 수를 저장할 배열
dp = [0] * (N+1)

#0, 1일 경우 0과 1 기본 세팅
if N >= 1:
    dp[1] = 1

#2이상일 경우 dp[i-1] + dp[i-2]
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])