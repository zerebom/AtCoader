N = int(input())
A = list(map(int, input().split()))
'''
1 bubbleSort(A, N) // N 個の要素を含む 0-オリジンの配列 A
2   flag = 1 // 逆の隣接要素が存在する
3   while flag
4     flag = 0
5     for j が N-1 から 1 まで
6       if A[j] < A[j-1]
7         A[j] と A[j-1] を交換
8         flag = 1
'''


def bubbleSort(A, N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                tmp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = tmp
                flag = 1
                count += 1
    print(' '.join(list(map(str, A))))
    print(count)


bubbleSort(A, N)
