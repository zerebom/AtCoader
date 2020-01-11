# from itertools import*
# n,*c=map(int,open(0).read().split())
# mod=10**9+7
# dif=[j-i for i,j in zip(c,c[1:])]
# fac=[1]*n
# for i in range(1,n):
# 	fac[i]=fac[i-1]*i%mod
# inv=[pow(i,mod-2,mod) for i in range(n)]
# acc_inv=list(accumulate(inv))
# ans=0
# for k in range(1,n):
# 	ans+=dif[k-1]*acc_inv[k]
# 	ans%=mod
# print(ans*fac[-1]%mod)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np
 
MOD = 10 ** 9 + 7
 
N = int(readline())
X = np.array(read().split(),np.int64)
 
def cumprod(A, MOD = MOD):
    #Lsq...平方根＋1?
    L = len(A); Lsq = int(L**.5+1)
    print('Lsq:',Lsq)
    #平方根にして、正方形になる
    A = np.resize(A, Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        A[:,n] *= A[:,n-1]; A[:,n] %= MOD
    for n in range(1,Lsq):
        A[n] *= A[n-1,-1]; A[n] %= MOD
    #ravel==flatten
    return A.ravel()[:L]

def make_fact(U, MOD = MOD):
    x = np.arange(U, dtype = np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact,fact_inv
 
U = 10 ** 5 + 5
fact, fact_inv = make_fact(U)
 
inv = np.zeros(U,np.int64)
inv[1:] = fact_inv[1:] * fact[:-1] % MOD
 
coef = inv[1:N].cumsum() % MOD
print('coef',coef)
print(fact,fact_inv)
answer = (np.diff(X) * coef % MOD).sum() % MOD
answer *= fact[N-1]; answer %= MOD
 
print(answer)