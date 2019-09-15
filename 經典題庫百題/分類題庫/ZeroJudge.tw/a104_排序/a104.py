import sys

for n in sys.stdin:
    ll = list(map(int, input().split()))
    print(*sorted(ll))
