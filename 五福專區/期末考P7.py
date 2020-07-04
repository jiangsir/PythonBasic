N = int(input())
ls = [int(x) for x in input().split()]

group = 0
for i in range(N):
    if ls[i]<0:
        continue
    else:
        x = i
        while i!=ls[x]:
            ls[x] = ls[x] - N
            x = ls[x] + N

        ls[x] = ls[x] - N
        group += 1

print(group)