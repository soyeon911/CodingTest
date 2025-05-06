# 1~N까지의 배열 형성
# K번째 원소 제거할 때마다 idx 초기화 해야함
# K번째를 세기 위해 현재 위치(0)에서 K-1만큼 이동한 후 len(arr)로 나눔 (원형 순환 때문)-> 리스트 넘어가면 다시 처음부터

N, K = map(int, input().split())
arr = list(range(1, N+1))
result = []

idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)
    result.append(arr.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")
