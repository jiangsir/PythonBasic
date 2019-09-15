# list # 串列 #反轉 # reversed

n = int(input())

rows = []
for i in range(n):
    rows.append(input())


for row in reversed(rows):
    print(row)

