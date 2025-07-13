N = int(input())
line = list(map(int, input().split()))

def snack(line):
    stack=[]
    expected = 1

    for student in line:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

        if student == expected:
            expected += 1

        else:
            stack.append(student)
    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1
    return "Nice" if not stack else "Sad"

print(snack(line))