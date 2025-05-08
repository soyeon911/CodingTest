# BFS로 트리 순회
# 노드들 queue에 넣고 방문할 때마다 큐에서 꺼냄. 그리고 인접한(neighbor)노드 queue에 삽입
# 큐가 빌 때까지 while문 돌리기

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)      # 각 노드에 부모 노드를 저장
visited = [False] * (N + 1) # 중복 방문 방지
queue = deque([1])          # 루트 노드 1부터 시작
visited[1] = True

#BFS 너비 우선 탐색
while queue:
    curr = queue.popleft()
    for neighbor in graph[curr]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = curr         # 부모 노드 기록
            queue.append(neighbor)          # 이웃의 이웃 노드도 탐색해야 하니 queue에 넣음

for i in range(2, N + 1):
    print(parent[i])