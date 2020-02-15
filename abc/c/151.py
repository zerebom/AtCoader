import numpy as np
N = int(input())
M = list(map(int, input().split()))
_min = np.inf
ans = 0

for i in range(N):
    if _min > M[i]:
        ans += 1
    _min = min(_min, M[i])

print(ans)
