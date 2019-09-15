#8. 找出最小值 
# 迴圈 #split()

import math

n = int(input())
min = math.inf
ll = [int(n) for n in input().split()]
for i in ll:
    if i < min:
        min = i
    
print(min)


'''

5
6 3 4 17 9

'''
