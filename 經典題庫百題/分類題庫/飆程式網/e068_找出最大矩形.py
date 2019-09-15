'''
#max #延伸:若是最後一個最大矩形, x*y >= max

'''
n = int(input())

max = -1
ans = ""
for _ in range(n):
    x, y = map(int, input().split())
    if x * y > max:
        max = x * y
        ans = str(x) + ' ' + str(y)

print(ans)
