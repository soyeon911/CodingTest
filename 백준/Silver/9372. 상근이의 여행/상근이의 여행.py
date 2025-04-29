# 여행하고 싶은 나라 = 노드 / 비행기 = 간선
# 트리구조
# 최소 비행기 종류의 개수를 구하라 -> 트리의 간선 수를 구하라 = 노드 수 - 1

T = int(input())
results = []

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        plane = (N - 1)
    results.append(plane)

for r in results:
    print(r)
