N = int(input())

def grade(N):
    if(N >= 90 and N <=100):
        return "A"
    elif(N >= 80 and N <= 89):
        return "B"
    elif(N >= 70 and N <= 79):
        return "C"
    elif(N >= 60 and N <= 69):
        return "D"
    else:
        return "F"

print(grade(N))