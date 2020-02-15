N = int(input())

A = [int(input()) for i in range(N)]

def insertionSort(A, n, g,cnt):
    for i in range(g,n-1):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt+=1
        A[j+g] = v
    print(' '.join(list(map(str,A))))
    return A,cnt
    

def shellSort(A, n):
    cnt = 0
    m = 2//2
    G = [0]
    for i in range(m):
        A,cnt=insertionSort(A, n, G[i],cnt)
    print(A,cnt)

shellSort(A,N)