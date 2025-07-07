# SJF 알고리즘 (Shortest Job First)
# 실행시간이 짧은 작업 우선 처리 -> 평균 대기 시간 최소화

N = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
response = 0

for time in times:
    response += time
    total += response

print(total)