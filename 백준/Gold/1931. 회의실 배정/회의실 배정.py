N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: (x[1], x[0]))

cnt = 0 
end_time = 0

for start, end in time:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)