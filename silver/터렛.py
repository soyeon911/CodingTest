import math
x1, y1, r1, x2, y2, r2 = input().split()

def turret(x1, y1, r1, x2, y2, r2):
    d = math.hypot(x2-x1, y2-y1)

    if d == r1 + r2:
        return 1
    elif d == abs(r1 - r2):
        return 1
    elif abs(r1 - r2) < d < (r1 + r2):
        return 2
    elif d > (r1 + r2):
        return 0
    else:  
        return 0
    
turret(x1, y1, r1, x2, y2, r2)