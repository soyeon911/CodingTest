N = int(input())

def yoon(N):
    if(N % 4 == 0):
        if(N % 100 != 0):
            return 1
        if(N % 400 == 0):
            return 1
        return 0
    else:
        return 0
    
print(yoon(N))