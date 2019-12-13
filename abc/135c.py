#https://atcoder.jp/contests/abc135/tasks/abc135_c

N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

ans=0
for i in range(len(B)):
    #勇者が全滅させたら、隣町から余力をとる
    if B[i]>A[i]:
        mod=min(A[i+1],B[i]-A[i])
        A[i+1]-=mod
        #この街と隣町
        ans+=int(A[i]+mod)
   
    #敵が余るときは勇者は力の限り全部倒す
    else:
        ans+=B[i]

print(ans)


