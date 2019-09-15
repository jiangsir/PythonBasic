s = input()

count = 0
for i,c in enumerate(s):
    if (i < len(s)-1 and s[i] == s[i+1]) or (i>0 and s[i] == s[i-1]):
        #print(c)
        count = count + 1
print(count)
