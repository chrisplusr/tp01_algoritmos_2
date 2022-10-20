def merge(A, P, left, middle, right):
    m = middle - left + 1
    n = right - middle

    A_L = [0] * m
    A_R = [0] * n

    P_L = [0] * m
    P_R = [0] * n

    for i in range(m):
        A_L[i] = A[left + i]
        P_L[i] = P[left + i]

    for i in range(n):
        A_R[i] = A[middle + 1 + i]
        P_R[i] = P[middle + 1 + i]

    i = 0
    j = 0
    k = left

    while i < m and j < n:
        if A_L[i] <= A_R[j]:
            A[k] = A_L[i]
            P[k] = P_L[i]
            i += 1
        else:
            A[k] = A_R[j]
            P[k] = P_R[j]
            j += 1
        k += 1

    while i < m:
        A[k] = A_L[i]
        P[k] = P_L[i]
        i += 1
        k += 1
    
    while j < n:
        A[k] = A_R[j]
        P[k] = P_R[j]
        j += 1
        k += 1

def merge_sort(A, P, left, right):
    if left < right:
        middle = (left + right) // 2

        merge_sort(A, P, left, middle)
        merge_sort(A, P, middle + 1, right)
        merge(A, P, left, middle, right)

