def minimum(l, h, A):
    if l == h:
        return A[l]
    if h - l == 1:
        return min(A[l], A[h])
    if h - l == 2:
        return min(A[l], A[l + 1], A[l + 2])

    first_mid = l + (h - l) // 3
    second_mid = l + 2 * (h - l) // 3

    return min(
        minimum(l, first_mid, A),
        minimum(first_mid + 1, second_mid, A),
        minimum(second_mid + 1, h, A),
    )


# Example usage
Array = [2, 9, 3, 4, 2, 0, 8, 3, 5]
print(minimum(0, len(Array) - 1, Array))
