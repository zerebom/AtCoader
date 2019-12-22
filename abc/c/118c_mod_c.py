# https://atcoder.jp/contests/abc118/tasks/abc118_c

import fractions as math
N = int(input())
'''abcdの最大公約数は,
abの公約数とｃの公約数＝abcの公約数になるのでこれを繰り返す'''
monsters = list(map(int, input().split()))
for i in range(N):
    if i != 0:
        monsters[i] = math.gcd(monsters[i - 1], monsters[i])
print(monsters[N - 1])
