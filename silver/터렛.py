import math
T = int(input())

def turret(x1, y1, r1, x2, y2, r2):
    d = math.hypot(x2 - x1, y2 - y1)

    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    elif d == r1 + r2:
        return 1
    elif d == abs(r1 - r2):
        return 1
    elif abs(r1 - r2) < d < (r1 + r2):
        return 2
    elif d > (r1 + r2):
        return 0
    else:
        return 0

results = []

# T번 반복해서 입력 받기
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    results.append(turret(x1, y1, r1, x2, y2, r2))
    
for result in results:
    print(result)