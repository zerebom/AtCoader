#B- 繰り返し２乗法
# https://atcoder.jp/contests/atc002/tasks/atc002_b

'''
>>...右シフト、指定した桁だけ右にずらす（つまり小さくなる)
<<...左シフト、その逆
'''

'''
n^k(mod m)を求める。

n^k={
    1:(k=0)
    (n^k/2)^2:(偶数)
    (n^k-2)*n:(奇数)
}
として再帰的に求める。これにより、O(log(k))回で求まる。

更に、大きい数字を使わないで済むように、
(a*b)mod m=((a mod m)*(b mod m))mod m
の等式を使用する。これで常にｍ未満になる。


'''


def pow_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return pow_mod(n, k - 1, m) * n % m
    else:
        t = pow_mod(n, k / 2, m)
        return t * t % m


def pow_mod_bin(n, k, m):
    '''
    二進数を用いたバージョン。
    kを二進数変換して１になったところの桁を掛け算する。
    (n^22=n^(2+4+16))
    ・組み合わせ、場合のかず
    ・素数pに対する逆元？
    ・行列の累乗などに対応
    '''
    r = 1
    for k in range(k,0 k >> 1):
        if(k & 1)r = (r * n) % m:
            n = (n * n) % m
        return r
