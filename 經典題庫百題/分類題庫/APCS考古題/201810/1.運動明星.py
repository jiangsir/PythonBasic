'''

'''

T = int(input())

total = 0
count = 0
for _ in range(T):
    moneys = [int(x) for x in input().split()]
    rank = moneys[0]

    total += moneys[rank]
    if moneys[rank] == max(moneys[1:]):
        count += 1

print(total)
print(count)
