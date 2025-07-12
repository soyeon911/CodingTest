N, S = map(int, input().split())
A = list(map(int, input().split()))

def summation(N, S, A):
    left = 0
    curr_sum = 0
    min_len = N + 1

    for right in range(N):
        curr_sum += A[right]

        while curr_sum >= S:
            min_len = min(min_len, right - left + 1)
            curr_sum -= A[left]
            left += 1

    return min_len if min_len != N + 1 else 0

print(summation(N, S, A))