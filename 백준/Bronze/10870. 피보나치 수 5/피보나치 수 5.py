N = int(input())

def fibbo(N):
    if N <= 1:
        return N
    return fibbo(N-1) + fibbo(N-2)

print(fibbo(N))