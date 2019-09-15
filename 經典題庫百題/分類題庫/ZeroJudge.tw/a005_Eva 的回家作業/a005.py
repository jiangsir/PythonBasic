import sys
for n in sys.stdin:
#    n = int(input())
    for i in range(int(n)):
        a, b, c, d = map(int, input().split())
        if (b-a) == (c-b) and (c-b) == (d-c):
            print(a, b, c, d, ((c-b)+d))
        elif (b/a) == (c/b) and (c/b)==(d/c):
            print(a, b, c, d, int(d * (d/c)) )
 