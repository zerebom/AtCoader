"""
配列の一番左の値Xを基準に
それより小さい値と大きい値を分けて再配置するコード
Xより小さい値はiより左に、大きい値は右側に配置する。
jは現在探索している添字
"""


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        # 小さい値があればそれより左に移動させる
        if A[j] <= x:
            # 添字iも大きくする
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return A, i + 1


# if __name__ == "__main__":
n = int(input())
A = list(map(int, input().split()))

A, I = partition(A, 0, n - 1)
# 標準出力に癖がある
# new_A=[]
# for i in range(n):
#     if i==I:
#         # new_A.append('[')
#         # new_A.append(str(A[i]))
#         # new_A.append(']')

#         print('[',end='')
#         print(A[i],end='')
#         print(']',end=' ')
#     else:
#         print(A[i],end=' ')
#         # new_A.append(str(A[i]))
# print()
# # print(' '.join(list(map(str, new_A))))

for i in range(n):
    if i:
        print(" ", end="")
    if i == I:
        print("[", end="")
    print(A[i], end="")
    if i == I:
        print("]", end="")
print()
