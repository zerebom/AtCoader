# https://atcoder.jp/contests/dp/tasks/dp_a
# https://qiita.com/drken/items/dc53c683d6de8aeacf5a#a-%E5%95%8F%E9%A1%8C---frog-1
# DPのコツ…再帰的な全探索のイメージを磨く！->dp[i]にはi番目までの探索過程がまとまっている。


def chmin(a, b):
    '''a>bならbを代入して返すメソッド'''
    if a > b:
        a = b
        return a
    else:
        return a


def main():
    '''もらうDPとして実装'''
    N = int(input())
    H = list(map(int, input().split()))
    # 最小なものにコストを書き換えたいので初期値は大きく取る
    dp = [1000000000] * N

    # 最初はコスト０
    dp[0] = 0
    for i in range(1, N):
        dp[i] = chmin(dp[i], dp[i - 1] + abs(H[i] - H[i - 1]))

        if i > 1:
            dp[i] = chmin(dp[i], dp[i - 2] + abs(H[i] - H[i - 2]))
    print(dp[i])


def rec_main():
    from typing import List
    '''メモ化再起として実装'''

    def _rec(dp: List, h: List, i: int, INF=1e10):
        # DP の値が更新されていたらそのままリターン
        if dp[i] < INF:
            return dp[i]
        if i == 0:
            return 0
        res = INF
        res = chmin(res, _rec(i - 1) + abs(h[i] - h[i - 1]))
        if i > 1:
            res = chmin(res, _rec(i - 2) + abs(h[i] - h[i - 2]))

        dp[i] = res
        return dp[i]

    def _main():
        N = int(input())
        H = list(map(int, input().split()))
        # 最小なものにコストを書き換えたいので初期値は大きく取る
        dp = [1000000000] * N
        print(_rec(dp=dp, h=H, i=N - 1))

    _main()
