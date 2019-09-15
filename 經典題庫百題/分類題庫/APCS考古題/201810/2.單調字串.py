import math

N = int(input())
min = math.inf
mins = chr(ord('Z')+1)
for _ in range(N):
    s = input()
    l = len(set(s))
    if l <= min:
        min = l
        if s < mins:
            mins = s

print(mins)

'''
5
PAPA
ABBB
ABBA
ABBAA
AACDW
'''
