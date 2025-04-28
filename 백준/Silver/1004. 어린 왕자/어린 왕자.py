# 출발점 혹은 끝점이 주어진 행성(원) 안에 있을 경우 무조건 지나게 된다.
# 주어지는 매 행성마다 점(출발점, 끝점)간 거리 d1, d2를 구하여 주어진 행성의 반지름^2 과의 관계를 통해 위치를 추정한다.
# d < r : 점이 원 내에 존재
# d > r : 점이 원 밖에 존재
# d = r : 점이 원 위에 존재
import sys
input = sys.stdin.readline

#
T = int(input())

result = []

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (x1 - cx)**2 + (y1 - cy)**2
        d2 = (x2 - cx)**2 + (y2 - cy)**2

        r_squared = r**2

        # 출발점과 끝점 중 최소 하나라도 원 내부에 있을 경우 무조건 한 번은 지나니 counting
        if(d1 < r_squared and d2 > r_squared) or (d1 > r_squared and d2 < r_squared):
            cnt += 1
    
    result.append(cnt)

for r in result:
    print(r)
