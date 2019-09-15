'''
#進位轉換 #二進位

'''

n = int(input())

def solution1(x):
    print(bin(x)[2:])

def solution2(x):
    ans = []
    if x == 0:
        print(0)
        return
    while x>0:
        ans.insert(0, x%2)
        x = x//2
    print(''.join(map(str, ans)))


for _ in range(n):
    x = int(input())
    #solution1(x)
    solution2(x)
