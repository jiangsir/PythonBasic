# 遞迴 #hanoi
'''
hanoi(n, A, B, C):
n==1: A 移到 C

else: hanoi(n-1, )

遞迴關係式：T(n) = T(n-1) + T(1) + T(n-1)，
且 T(1) = 1 ；則 T(n) = 2*T(n-1) + T(1) ，
解出 T(n) 為 2^n -1

'''

count = 0

def hanoi(n, A, B, C):
    global count
    if n == 1:
        count += 1
        print(n, A, '->', C)
    else:
        hanoi(n-1, A, C, B)
        count += 1
        print(n, A, '->', C)
        hanoi(n-1, B, A, C)


hanoi(3, 'A', 'B', 'C')
print('共移動', count, '次')

