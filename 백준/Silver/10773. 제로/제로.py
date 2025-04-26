import sys

input = sys.stdin.readline
stack = []
N = int(input())

for _ in range(N):
    element = int(input())

    if element != 0:
        stack.append(element)
    else:
        if stack:
            stack.pop()
        
print(sum(stack))