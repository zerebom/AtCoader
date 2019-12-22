
def chmin(a,b):
    '''a>bならbを代入して返すメソッド'''
    if a>b:
        a=b
        return a
    else:
        return a


N=int(input())
H=list(map(int,input().split()))
#最小なものにコストを書き換えたいので初期値は大きく取る
dp=[1000000000]*N

#最初はコスト０
dp[0]=0
for i in range(1,N):
    dp[i]=chmin(dp[i],dp[i-1]+abs(H[i]-H[i-1]))
    
    if i>1:
        dp[i]=chmin(dp[i],dp[i-2]+abs(H[i]-H[i-2]))
print(dp[i])
