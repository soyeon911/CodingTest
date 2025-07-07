N = int(input())
result = []

for _ in range(N):
    age, name = input().split()
    result.append((int(age), name))

result.sort(key=lambda x: x[0])

for age, name in result:
    print(age, name)