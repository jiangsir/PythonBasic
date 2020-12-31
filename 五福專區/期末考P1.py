n = int(input())
for i in range(n):
    p1, p2, p3 = [int(x) for x in input().split()]
    if p1!=p2 and p2!=p3 and p1!=p3:
        print('YES')
    else:
        print('NO')
