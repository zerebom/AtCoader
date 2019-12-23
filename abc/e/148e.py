from math import log10

N = int(input())
digit = len(str(N))
ans = 0
for d in range(1, digit):
    print(N // (10**d))
    ans += (N // (10**d))
    ans+=(N//(10*(5**d)))

print(ans)
# ans=1
# for i in range(2,101,2):
#     print(i)
#     ans=ans*i

# print(ans)
