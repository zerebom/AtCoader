'''
dp[ i ][ sum_w ] := i-1 番目までの品物から重さが sum_w 以下となるように選んだときの、価値の総和の最大値
'''

N,W = list(map(int, input().split()))

weight = []
value=[]
dp=[[0 for i in range(N)] for j in range(W)]

for i in range(N):
    w,v = list(map(int, input().split()))
    weight.append(w)
    value.append(v)

for i in range(N):
    for sum_w in range(W):
        if sum_w-weight[i]>=0:
            #商品i+1を追加した時の価値、としなかった時の価値。
            dp[i+i]=max(dp[i+1][sum_w], dp[i][sum_w-weight[i]+value[i]]
        #商品を追加した時の価値と、しなかった時の価値の大きい方を選ぶ
        dp[i+1]=max(dp[i+1][sum_w],dp[i][sum_w])

            
