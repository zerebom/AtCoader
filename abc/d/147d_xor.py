# https://atcoder.jp/contests/abc147/tasks/abc147_d

import numpy as np
N = int(input())
'''
XORはビット演算子同士で干渉しない。
なので、一つずつ見ていく
例えばあるBitで０が2個、1が3個あった場合はその部分の,
0と1の組み合わせは2*3で6個ある。
これにBitをかけてあまりを求めればOK
'''
#np arrayにすぐできる
A = np.fromstring(input(), dtype=np.int64, sep=' ')

result = 0
for bit in range(60):
    #一番下の桁が1かどうかをカウント
    c = int((A & 1).sum())
    #+=みたいな感じ、inplace
    A >>= 1
    # 1<<bit...1がbitの数だけ左にずれる。1000みたいな
    #0の数×1の数×ビットをシフトした数
    result = (result + c * (N - c) * (1 << bit)) % 1000000007
print(result)
