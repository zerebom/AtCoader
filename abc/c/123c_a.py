#https://atcoder.jp/contests/abc123/tasks/abc123_c
#C:A
from math import ceil
N=int(input())
T=[]
for _ in  range(5):
    T.append(int(input()))

min_t=min(T)
# if min_t>=N:
#     print(5)
# else:
print(ceil(N/min_t+4))
