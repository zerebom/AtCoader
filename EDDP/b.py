# DPの計算量…DPテーブルのノードの数＋エッジの数
# https://atcoder.jp/contests/dp/tasks/dp_b
# 理屈はあってるが、PythonなのでTLEになります…


'''もらうDPとして実装'''
N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
# 最小なものにコストを書き換えたいので初期値は大きく取る
dp = [float('inf')] * N

# 最初はコスト０
dp[0] = 0
for i in range(1, N):
    dp[i] = min(dp[j] + abs(H[i] - H[j]) for j in range(max(i - K, 0), i))
print(int(dp[i]))
