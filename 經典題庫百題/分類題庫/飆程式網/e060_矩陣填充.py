'''
https://zerojudge.tw/ShowProblem?problemid=e060

#建立二維陣列 #雙層迴圈 #*解包

'''

row, col = map(int, input().split())

mx = [['' for _ in range(col)] for _ in range(row)]
for r in range(row):
    for c in range(col):
        mx[r][c] = '('+str(r) +','+ str(c) +')'

for li in mx:
    print(*li)
