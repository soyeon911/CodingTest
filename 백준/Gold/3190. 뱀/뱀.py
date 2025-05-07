# 큐(deque)로 뱀의 몸통 저장, 방향 전환 dict() 처리, 충돌판정 (1. 테두리 닿을 때, 2. 지 몸통에 닿을 때)

from collections import deque

N = int(input())
K = int(input())
apples = set(tuple(map(int, input().split())) for _ in range(K))

L = int(input())
turn = dict()       # key(X), value(C)
for _ in range(L):
    X, C = input().split()
    turn[int(X)] = C

time = 0
dir = 0                 # default 동쪽
snake = deque([(1, 1)])
occupied = set([(1, 1)])
dx = [0, 1, 0, -1]      # 동 남 서 북
dy = [1, 0, -1, 0]      # 프로그램 내에서 좌표 계는 행-열 반대

while True:
    time += 1

    # 뱀 머리 이동하고 난 후 좌표
    head_x, head_y = snake[0]
    nx = head_x + dx[dir]
    ny = head_y + dy[dir]

    # 게임 종료 조건 (테두리에 닿을 때) or (지 몸에 닿을 때)
    if not(1 <= nx <= N and 1 <= ny <= N) or (nx, ny) in occupied:
        print(time)
        break

    # 뱀의 머리 이동
    snake.appendleft((nx, ny))
    occupied.add((nx, ny))

    # 사과 있으면 사과 지우고 꼬리는 그대로 (tail 유지, head + 1)
    if(nx, ny) in apples:
        apples.remove((nx, ny))
    
    # 사과 없으면 꼬리 제거해서 뱀의 길이 유지 (tail - 1, head + 1)
    else:
        tail = snake.pop()
        occupied.remove(tail)

    # 시간 초 후에 따라 방향 변환
    if time in turn:
        if turn[time] == 'L':
            dir = (dir - 1) % 4
        elif turn[time] == 'D':
            dir = (dir + 1) % 4