N, M = list(map(int, input().split()))


ACd = [0] * N
whenACd = [0] * N

pena = 0
I,X=[],[]
for m in range(M):
    i, x = list(map(str, input().split()))
    I.append(i)
    X.append(x)

for m,(i,x) in enumerate(zip(I,X)):
    if x == 'AC' and ACd[int(i) - 1] == 0:
        ACd[int(i) - 1] = 1
        whenACd[int(i) - 1] = m

for m,(i,x) in enumerate(zip(I,X)):
    if x == 'WA' and whenACd[int(i) - 1] > m:
        pena += 1

print(sum(ACd), pena)

# 3 6
# 1 WA
# 3 WA
# 1 AC
# 2 WA
# 2 AC
# 2 WA

# 100000 6
# 7777 AC
# 7778 WA
# 7779 WA
# 7779 AC
# 7777 AC
# 7777 AC