a, b, c = map(int, input().split())
a, b, c = map(bool, [a, b, c])
i = True
if(a and b) == c:
    print("AND")
    i = False
if(a or b) == c:
    print("OR")
    i = False
if(a ^ b) == c:
    print("XOR")
    i = False
if i:
    print("IMPOSSIBLE")
