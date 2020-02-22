# https://atcoder.jp/contests/abc154/tasks/abc154_d

N, K = map(int, input().split())
s = list(map(int, input().split()))

# 初期値として0~Kのサイコロの目を最大値として保持しておく
max = x = sum(s[:K])
for i in range(N - K):
    x += (s[K + i] - s[i])
    if max < x:
        max = x

# 期待値はサイコロの目の数の合計+1*サイコロの数/2
print((max + K) / 2)
