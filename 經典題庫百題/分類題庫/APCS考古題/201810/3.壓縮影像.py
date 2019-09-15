'''
#遞迴 #global
'''


s = input()
N = int(input())
index = 0

def count(n):
    global index
    if s[index] == '0':
        return 0
    elif s[index] == '1':
        return n ** 2
    else:
        ans = 0
        for _ in range(4):
            index += 1
            ans += count(n//2)
        return ans
        
print(count(N))

'''
2200101020110
4

2020020100010
8

20100
4

1
8

0
8
'''
