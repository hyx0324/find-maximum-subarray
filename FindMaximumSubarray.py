import numpy as np

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0

    for i in range(mid, low-1, -1):
        sum += A[i]

        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0

    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]

    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum

        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    A_size = 16
    A = list(np.random.randint(-100, 100, size=A_size))
    low, high, sum = find_maximum_subarray(A, 0, len(A)-1)

    print('The original list is:', A)
    print('\nThe maximum subarray is:', A[low: high+1])
    print('\nThe sum is:', sum)