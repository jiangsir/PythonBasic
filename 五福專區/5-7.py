n = int(input())

dd = {}
for i in range(n):
    pid, name = input().split()
    dd[pid] = name

def sortkey2(item):
    return item[0][0]

def sortkey1(item):
    return item[0][8]


items = sorted(dd.items(), key=sortkey2)
items = sorted(items, key=sortkey1)

for item in items:
    print(item[0][8]+": "+item[1])