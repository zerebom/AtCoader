N=int(input())
A=list(map(int,input().split()))

def selectionSort(A,N):
    count = 0
    for i in range(N):
        mini=i
        for j in range(i,N):
            if A[j]<A[mini]:
                mini=j
        if i!=mini:
            tmp = A[i]
            A[i]=A[mini]
            A[mini] = tmp
            count += 1


    print(' '.join(list(map(str, A))))
    print(count)

selectionSort(A,N)