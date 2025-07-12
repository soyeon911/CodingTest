def balanced(line):
    stack=[]
    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

while True:
    line = input()
    if line == ".":
        break
    print(balanced(line))