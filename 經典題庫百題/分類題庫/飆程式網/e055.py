n = int(input())

ss = []
for i in range(n):
    ss.append(input())

for s in ss:
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')
