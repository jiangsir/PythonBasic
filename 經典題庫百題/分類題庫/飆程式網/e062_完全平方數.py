'''
#數學函數 #無條件捨去

'''

import math

N = int(input())

for i in range(N):
    x = int(input())
    ans = math.sqrt(x)
    if ans == int(ans):
        print('Yes')
    else:
        print('No')
