s = input()

s2 = s[len(s)//2:]
if len(s)%2==0 and s[:len(s)//2] == s2[::-1]:
    print('Yes')
    print(s[:len(s)//2])
else:
    print('No')