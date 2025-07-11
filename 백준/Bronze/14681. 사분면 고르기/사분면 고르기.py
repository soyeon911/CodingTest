X = int(input())
Y = int(input())

def function(X, Y):
    if(X > 0 and Y > 0):
        return 1
    if(X > 0 and Y < 0):
        return 4
    if(X < 0 and Y > 0):
        return 2
    if(X < 0 and Y < 0):
        return 3
print(function(X, Y))