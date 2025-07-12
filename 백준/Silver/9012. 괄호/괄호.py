T = int(input())

def is_vps(ps):
    stack=[]
    for char in ps:
        if char == "(":
            stack.append(ps)
        else:
            if stack:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

for _ in range(T):
    ps = input().strip()
    print(is_vps(ps))
