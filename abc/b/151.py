a, b = list(map(int, input().split()))
if a < b:
    print(str(a) * b)
else:
    print(str(b) * a)
N,K,M=list(map(int,input().split()))
A=list(map(int,input().split()))

ans=N*M-sum(A)
if ans<=0:
    print(0)
elif ans>K:
    print(-1)
else:
    print(ans)
