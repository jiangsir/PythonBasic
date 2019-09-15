from collections import Counter

n = input()
ll = map(int, input().split())
most = Counter(ll).most_common()

max = most[0][1]
ans = []
for m in most:
    if m[1] == max:
        ans.append(m[0])

print(" ".join(str(s) for s in sorted(ans)))
