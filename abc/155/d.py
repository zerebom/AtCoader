import numpy as np

'''
np.searchsorted([1,2,3,4,5], [-10, 10, 2, 3])
array([0, 5, 1, 2])
left	a[i-1] < v <= a[i]
right	a[i-1] <= v < a[i]
リストがどの番号に挿入されるかを返す
'''
n, k = map(int, input().split())
A = np.array(sorted(np.array(input().split(), np.int64)))


posA = A[A > 0]
negA = A[A < 0]
zeros = (A == 0).sum()

left = -10**18
right = 10**18

# 二分探索を続ける。k番目の値=countになったら終わり。
# countはleft~rightの中でどれだけ組み合わせがあるかを保持している。
while left + 1 < right:
    mid = (left + right) // 2
    count = 0
    if mid >= 0:
        count += zeros * n
    pos = mid // posA
    print('pos:', pos)
    idxs = np.searchsorted(A, pos, side='right')
    print(posA, pos, negA)

    count += idxs.sum()
    print('idx pos:', idxs)

    neg = -(mid // -negA)
    print('neg:', neg)
    idxs = n - np.searchsorted(A, neg, side='left')
    count += idxs.sum()
    print('idx neg:', idxs)
    dup = (A**2 <= mid).sum()
    count -= dup
    count //= 2

    if count >= k:
        right = mid
    else:
        left = mid

print(right)
