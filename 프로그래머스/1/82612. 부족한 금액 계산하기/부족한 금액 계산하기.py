def solution(price, money, count):
    pay = 0
    for i in range(1, count + 1):
        pay += price * i
    return max(0, pay- money)