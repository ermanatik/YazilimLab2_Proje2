def brute_force_min_difference(arr):
    n = len(arr)
    min_diff = float('inf')

    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff

        return min_diff


def sorted_min_difference(arr):
    arr.sort()
    n = len(arr)
    min_diff = float('inf')

    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff

    return min_diff
