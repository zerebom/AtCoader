#range R+1に注意。 C:B
'''
数十万オーダーなら全探索できることに注意
'''
L, R = list(map(int, input().split()))

ans = 2019
if R-L>2019:
    print(0)
else:
    for l in range(L, R):
        for r in range(l + 1, R+1):
            tmp = (l * r) % 2019
            # tmp = ((l%2019) * (r%2019)) % 2019
            ans = min(ans, tmp)
            if ans == 0:
                break
    print(ans)
