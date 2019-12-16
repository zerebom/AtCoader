import numpy as np
from math import factorial as fac


def ans():
    '''
    Fxまでの行き方はF(x-1)+F(x-2)がある。
    フィボナッチ数の求め方の式と同様。
    DPを使えばO(N)で求まる。
    壊れた階段には遷移しないように改造すればOK
    '''
    MOD = 10**9 + 7
    N, M = [int(s) for s in input().split()]
    #行ってはいけないところには0がはいる
    ls = [1 for _ in range(N + 1)]
    for i in range(M):
        ls[int(input())] = 0
    
    for n in range(2, N + 1):
        if ls[n] != 0:
            #(n*m)mod k ==(n(mod k)*m(mod k))
            ls[n] = (ls[n - 1] + ls[n - 2]) % MOD
    print(ls[N])


def myans():
    '''
    壊れた階段までの通り道の場合のかずをそれぞれ掛け算すれば良いと考えた。
    奇数偶数の処理、i=0の時などの場合わけでグダグダになった
    '''
    N, M = list(map(int, input().split()))
    A = []
    for _ in range(M):
        A.append(int(input()))
    ans = 0
    for i in range(M - 1):
        if A[i] + 1 == A[i + 1]:
            ans = None

    steps = np.zeros(M)
    if ans != None:
        for i in range(M):
            if i == 0:
                diff = A[0]
            else:
                diff = A[i] - A[i - 1] - 1
            odd = diff % 2
            # 2の最大数
            two = ()
            # j...２じゃない数
            for j in range((diff // 2) + 1):
                print(j)
                two = (diff // 2) - j
                one = 2 * j + odd
                print(two, one)
                steps[i] += fac(two + one) / (fac(two) * fac(one)) + 1
        print(steps)
        print(np.prod(steps) % 10000000007)
