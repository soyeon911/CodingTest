# 옮길 수 있는 포대는 3, 5kg
# 5kg 최대한 많이 쓰고 나머지는 3kg로 
# 0까지 내려갔는데도 안 되면 -1

N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)