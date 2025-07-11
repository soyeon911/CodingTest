a, b, c = map(int, input().split())

def dice(a, b, c):
    if(a == b == c):
        return 10000 + a*1000
    if(a == b != c):
        return 1000 + a*100
    if(a != b == c):
        return 1000 + b * 100
    if(a == c != b):
        return 1000 + a* 100
    if(a != b != c):
        return max(a, b, c)*100
    
print(dice(a, b, c))