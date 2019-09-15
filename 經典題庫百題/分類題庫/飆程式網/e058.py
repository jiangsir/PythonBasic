'''

'''

n = int(input())

flag = False
for x in range(2, n+1):
    if flag or x > n:
        break
    for y in range(1, n):
        if x ** y == n:
            print(x, y)
            flag = True
            break
        if x ** y > n:
            break
