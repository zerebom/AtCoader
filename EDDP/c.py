# 前日の行動と、当日の行動から最大値を求める。


N = int(input())
dp = [[0, 0, 0] for i in range(N)]
H = []


for i in range(N):
    l = list(map(int, input().split()))
    H.append(l)

dp[0] = [H[0][0], H[0][1], H[0][2]]

for i in range(1, N):
    # 現在の選択肢
    for k in range(3):
        # 過去の選択肢
        for j in range(3):
            if j == k:
                continue
            else:
                dp[i][j] = max(dp[i][j], (dp[i - 1][k] + H[i][j]))
print(max(dp[N - 1]))
