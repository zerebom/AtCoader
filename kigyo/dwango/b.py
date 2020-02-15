from statistics import mean
from math import factorial
import numpy as np
from itertools import*

# def myans():
#     N = int(input())
#     H = list(map(int, input().split()))
#     MOD = 1000000000+7
#     diff=[]
#     for i in range(N-1):
#         diff.append(H[i+1]-H[i])

#     diff=np.array(diff)
#     multi=np.array([mean(list(range(1,i+1))) for i in range(1,N)])
#     # print(multi)
#     # print(diff)
#     print(int(np.sum(diff*multi)*(factorial(N-1)%MOD)%MOD))

#src:https://atcoder.jp/contests/dwacon6th-prelims/submissions/9426491
#最初の値はnに入って、その他はcに入る
n,*c=map(int,open(0).read().split())
mod=10**9+7
dif=[j-i for i,j in zip(c,c[1:])]
fac=[1]*n
#階乗。毎回modで割っても大丈夫
for i in range(1,n):
    fac[i]=fac[i-1]*i%mod

inv=[pow(i,mod-2,mod) for i in range(n)]
#itertoolより。
acc_inv=list(accumulate(inv))
ans=0
for k in range(1,n):
    ans+=dif[k-1]*acc_inv[k]
    ans%=mod
print(ans*fac[-1]%mod)
