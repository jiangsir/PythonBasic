'''
#數值交換

'''

def solution1(s):
    a1, b1, a2, b2 = map(int, s.split())

    if a1>a2:
        a1, a2 = a2, a1
        b1, b2 = b2, b1
    if a2 <= b1:
        print('Yes')
    else:
        print('No')



n = int(input())
for i in range(n):
    solution1(input())
