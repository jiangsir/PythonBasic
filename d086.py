s = input().strip()
s = s.upper()

table = 'ABCDEFG'
ans = 0
for c in s:
    if c not in table:
        print('Fail')
        break
    ans = ans + table.find(c)+1
    