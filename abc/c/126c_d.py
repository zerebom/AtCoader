N,K = list(map(int, input().split()))

'''
でたサイコロの目をXとする
X>Kの部分は全部1
0<X<N-Kの時はでた目によって成功確率が違う
2の何乗か*

場合分けをしなくて済むように、変数を減らせるようによく考える。
繰り返しを使う。min,maxを使う
'''
ans=0
exp_K=len(format(K, 'b'))-1
idx_K=K/(2**exp_K)

#サイコロの麺の方が多い時
if N>K:
    ans=max(0,(N-K)/N)
    for X in range(2,K):
        print(X)
        exp_X=len(format(X, 'b'))-1
        idx_X=X/(2**exp_X) if exp_X!=0 else X
        print(exp_K,idx_K,exp_X,idx_X)

        bigger=int(idx_K>idx_X)
        tmp_ans=(1/N)/(2**(exp_K-exp_X+bigger))
        print('anss',tmp_ans,ans)
        ans+=tmp_ans

    print(ans)
#目標スコアの方が高い場合
else:
    for X in range(2,N+1):
        print(X)
        exp_X=len(format(X, 'b'))-1
        idx_X=X/(2**exp_X) if exp_X!=0 else X
        print(exp_K,idx_K,exp_X,idx_X)
        bigger=int(idx_K>idx_X)
        tmp_ans=(1/N)/(2**(exp_K-exp_X+bigger))
        print('anss',tmp_ans,ans)
        ans+=tmp_ans
    print(ans)


K = map(int, input().split())
N,K = list(map(int, input().split()))
win = 0
#全事象に対して
for i in range(N):
    #確率
    j = 1
    k = j + i
    #現在のスコア<目的スコアになるまで
    while k < K:
        #コイントスごとに確率は1/2になる
        j /= 2
        #現在のスコアは2倍になる
        k *= 2
    #while文を通らなかったものは１が足される
    win += j
print(win/N)
    