s = input()

A = 0
B = 0
for i, c in enumerate(s):
    if i%2==0:
        A += int(c)
    else:
        B += int(c)
print(abs(A-B))