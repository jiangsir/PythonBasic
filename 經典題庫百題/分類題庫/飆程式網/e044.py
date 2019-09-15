t = int(input())
for i in range(t):
    ans = [0 for n in range(10)]
    s = input()
    for c in s:
        ans[int(c)] = ans[int(c)] + 1
    print(s, ' '.join(str(x) for x in ans))
