# 명령어에 따른 스택 설계
# push 연산 이외의 명령어가 들어오면 results에 결과물 입력

import sys
input = sys.stdin.readline

N = int(input())
stack = []
results = []

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        results.append(stack.pop() if stack else -1)
    elif command[0] == "size":
        results.append(len(stack))
    elif command[0] == "empty":
        results.append(0 if stack else 1)
    elif command[0] == "top":
        results.append(stack[-1] if stack else -1)

for r in results:
    print(r)