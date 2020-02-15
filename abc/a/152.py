
H = list(map(str,input().split()))
W = list(map(int, input().split()))

color = input()

# print(H,W,color)
idx = H.index(color)

W[idx] = W[idx] - 1

print(W[0], W[1])
