import numpy as np
H = int(input())
W = int(input())
N = int(input())

h=max(H,W)
print(int(np.ceil(N/h))