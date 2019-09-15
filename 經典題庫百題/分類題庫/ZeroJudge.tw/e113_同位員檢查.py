s = input()

count = 0
for i in s:
    if i == '1':
        count = count + 1

if count%2==0:
    print(s+'1')
else:
    print(s+'0')
