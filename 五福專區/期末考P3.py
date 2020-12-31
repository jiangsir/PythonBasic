n = int(input())
for i in range(n):
    total = int(input())
    if total%2==1:
        print('0 0')
    else:
        # total = 2 * j + 4 * t
        tu = total // 4
        ji = total % 4 / 2
        print(int(tu+ji), total//2)
