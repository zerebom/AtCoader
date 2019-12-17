# https://atcoder.jp/contests/abc131/tasks/abc131_c

'''
B以下のC,Dの倍数の個数は(B//C)+(B//D)-(B//(C,Dの最小公倍数の数＝L))
LはCD/(C,Dの最大公約数)より求まる。
Bの条件に当てはまる値からA−1いかの条件に当てはまる値を引けば良い

Pythonで最大公約数・最小公倍数を求める方法
https://qiita.com/Dexctersu/items/43d844db0e751b23b3b7

ユークリッドの互除法について
http://arithmetic.archivs.org/sansugaku/sansugaku-06.html
'''


import fractions as math
def gcd(a, b):
    '''ユークリッド互除法を使った最大公約数の求め方'''
    while b != 0:
        a, b = b, a % b
    return(a)


def lcm(a, b):
    '''最小公倍数の求め方'''
    return a * b // gcd(a, b)


A, B, C, D = list(map(int, input().split()))

lcmCD = lcm(C, D)

divB = (B // C) + (B // D) - (B // lcmCD)
divA_1 = ((A - 1) // C) + ((A - 1) // D) - ((A - 1) // lcmCD)
print((B - A) - (divB - divA_1) + 1)

#別解
a, b, c, d = map(int, input().split())

def F(n, c, d):
    x = n
    x -= n // c
    x -= n // d
    lcm = c * d // math.gcd(c, d)
    x += n // lcm
    return x


print(F(b, c, d) - F(a - 1, c, d))
