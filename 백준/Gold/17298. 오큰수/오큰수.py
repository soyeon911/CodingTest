# NGE 배열엔 결과값을, stack 배열에는 A의 인덱스 값을 저장
# 현재 값이 스택의 top에 위치한 값보다 크다면 pop 이후 NGE 배열에 삽입
# pop 한 이후 현재 인덱스 stack에 push

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
NGE = [-1] * n
stack = []

for i in range(n):
    while stack and A[i] > A[stack[-1]]:
        idx = stack.pop()
        NGE[idx] = A[i]
    stack.append(i)

print(*NGE)