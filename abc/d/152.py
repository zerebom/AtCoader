N, K = list(map(str, input().split()))
P = list(map(int, input().split()))
K = int(K)

ans = 0
for i in range(len(P) - K - 1):
    if i == 0:
        ans = sum(P[i:i+K])

    else:
        diff=P[i+K] - P[i]
        print('diff',diff)
        # if diff>0:
        ans = ans + diff
        print('ans',ans)
        print('P',P[i:i+K],sum(P[i:i+K]))


print((ans + K) / 2)
print(ans + K)

