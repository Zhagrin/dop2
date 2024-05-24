import math
from random import randint
from statistics import mean
M = 0
N = 10000
S = 0
A = [randint (1, 100000)
     for i in range(N)]
print(A)
for j in A:
    if j % 5 == 0:
        M += j
        S += +1
        continue
K = M / S
for k in A:
    if k > K:
        print('корень', k, k ** 0.5)