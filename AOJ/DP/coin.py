# import numpy as np
# url:https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_A

N, M = list(map(int, input().split()))
C = list(map(int, input().split()))
T = [float('inf')] * (N+1)
T[0] = 0

for i in range(M):
    for j in range(C[i], N + 1):
        T[j] = min(T[j], T[j - C[i]] + 1)

print(T[-1])
