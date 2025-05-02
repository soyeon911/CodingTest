# 뽑고 싶은 숫자들 target_list
# 맨 앞이 target이라면 0번 연산(pop left)
# 아니라면 - 왼쪽으로 돌리기(2번 연산), - 오른쪽으로 돌리기(3번 연산)
# 둘 중 더 적은 연산을 선택 how? target 위치를 전체 큐 길이를 이용해서 구하고 인덱스가 큐 길이 절반 이하면 왼쪽

from collections import deque

N, M = map(int, input().split())
targets = list(map(int, input().split()))
queue = deque(range(1, N+1))

cnt = 0

for target in targets:
    idx = queue.index(target)

    # 인덱스가 큐 길이 절반 이하면
    if idx <= len(queue) // 2:
        queue.rotate(-idx)  # 왼쪽으로 idx칸 이동
        cnt += idx
    else:
        queue.rotate(len(queue) - idx)
        cnt += (len(queue) - idx)

    queue.popleft()     # 첫 번째 요소 제거

print(cnt)