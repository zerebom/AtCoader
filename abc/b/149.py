A,B,K = list(map(int, input().split()))

if K>A:
    K2=K-A
    if K2>B:
        print(0,0)
    else:
        print(0,B-K2)
else:
    print(A-K,B)
