# https://atcoder.jp/contests/abc130/tasks/abc130_c
# C - Rectangle Cutting
#B
'''
どんな点を通っても中心とその点の二点を通れば、
長方形は半分に切断することができる
'''

W, H, x, y = list(map(int, input().split()))

half = W * H / 2
if (W / 2) == x and (H / 2) == y:
    ans = 1
else:
    ans = 0

print(half, ans)
