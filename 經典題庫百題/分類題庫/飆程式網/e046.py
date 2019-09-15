s = input()
ll = list(s)
for i, c in enumerate(ll):
    if c.isupper():
        ll[i] = c.lower()
    else:
        ll[i] = c.upper()
print("".join(ll))
