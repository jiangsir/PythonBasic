
a, b, c = sorted(map(int, input().split()))
print(a, b, c)
if a+b < c:
    print('No')
elif a*a+b*b < c*c:
    print('Obtuse')
elif a*a+b*b > c*c:
    print('Acute')
else:
    print('Right')
