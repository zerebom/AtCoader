# https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_B

N, W = list(map(int, input().split()))
I = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0 for i in range(N + 1)] for j in range(W + 1)]

# for i in range(N):
#     value, weight = I[i]
#     print(value,weight,dp)
#     for sum_w in range(W):
#         if sum_w - weight >= 0:
#             dp[i + 1] = max(dp[i][sum_w], dp[i + 1][sum_w - weight] + value)

# ans = 0
# for i in range(W + 1):
#     ans = max(ans, dp[i])

# print("%d" % (ans))
# dp = [-float('inf')]*(W+1)
# dp[0] = 0

# for i in range(N):
#     value, weight = I[i]
#     print(value,weight,dp)
#     for sum_w in range(W+1):
#         if sum_w - weight >= 0:
#             dp[sum_w] = max(dp[sum_w], dp[sum_w-weight] + value)

# ans = 0
# for i in range(W + 1):
#     ans = max(ans, dp[i])

# print("%d" % (ans))

N, W = map(int, input().split())
dp = [[0 for i in range(W + 1)]for j in range(N + 1)]
goods = []
for i in range(N):
    v, w = map(int, input().split())
    goods.append([v, w])


for i in range(N):
    v = goods[i][0]
    w = goods[i][1]
    for j in range(W + 1):
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
        next_w = j + w
        next_v = dp[i][j] + v
        if(next_w <= W and next_v > dp[i + 1][next_w]):
            dp[i + 1][next_w] = next_v

ans = 0
for i in range(W + 1):
    ans = max(ans, dp[N][i])
print(ans)
