A, B, C = input().split()   # 입력받은 세 문자 spilt
A = int(A)
B = int(B)
C = int(C)

print(((A+B)%C))
print(((A%C)+(B%C))%C)
print(((A*B)%C))
print(((A%C)*(B%C))%C)