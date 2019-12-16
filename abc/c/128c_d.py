#https://atcoder.jp/contests/abc128/tasks/abc128_c


def myans():
    N, M = [int(s) for s in input().split()]
    K = []
    S = []

    '''
    引数が多すぎてゴチャゴチャして死んだ。
    '''
    for _ in range(M):
        k, *s = list(map(lambda x:int(x)-1, input().split()))
        K.append(k)
        S.append(s)

    P = list(map(int, input().split()))
    ans=0
    print(f'S:{S}')
    #スイッチのつき方ごと
    for n in range((1 << N) - 1, -1, -1):
        bin_S=[(n >> i) & 1 for i in range(N)]
        tmp_p=0
        print()
        print(f'あるつき方,bin_S:{bin_S}')
        #スイッチがついてるかの2進数
        #各電球について
        for m in range(M):
            print(f'ある電球について,m:{m},Pm:{P[m]},K[m]:{K[m]}')
            OK=True
            while OK:
                #各電球の各スイッチについて:K[m]...その電球に何個スイッチがついているか
                #S[m][k],電球S[m]のk番目のスイッチ
                for k in range(K[m]):
                    print(f'あるスイッチについて,k:{k}')
                    print(f'S[m][k]:{S[m][k]}')
                    tmp_p+=bin_S[S[m][k]]
                if tmp_p%2!=P[m]:
                    OK=False
                    break
                else:
                    break
        print(f'OK:{OK}')
        ans+=int(OK)
    print(ans)
            
def ans():
    n, m = map(int, input().split())
    s = []
    for i in range(m):
        st = list(map(int, input().split()))
        s.append(st[1 :])
    p = list(map(int, input().split()))
    
    ans = 0
    #あるつき方について
    for i in range(1 << n):
        al = True
        #つき方二進数
        v = [bool(i & (1 << x)) for x in range(n)]
        #電球全体
        for j in range(m):
            #onになってるスイッチの個数
            num = 0
            #スイッチの番号
            for t in s[j]:
                num += v[t - 1]
            if p[j] != num % 2:
                al = False
        ans += al
    print(ans)            


            
