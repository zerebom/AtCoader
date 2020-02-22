# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b

import sys
# ↓TLE涙
# N = int(input())
# X, L = [], []

# for i in range(N):
#     x, l = list(map(int, input().split()))
#     X.append([x, l])
#     X.sort(key=lambda x: x[0], reverse=False)

# L = [x[1] for x in X]
# X = [x[0] for x in X]

# ans = 0
# cur = -float('inf')
# for i in range(N):
#     if (cur <= X[i] - L[i]):
#         ans += 1
#         cur = X[i] + L[i]
# print(ans)

import sys
N = int(input())
a = sorted([(x + l, x - l) for x, l in (map(int, l.split()) for l in sys.stdin)])

last = a[0][0]
ans = 1

for r, l in a[1:]:
    if last <= l:
        ans += 1
        last = r

print(ans)
