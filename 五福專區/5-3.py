# b964: 第 1 題 成績指標
n = input()
ll = sorted([int(x) for x in input().split()])
print(*ll)

if ll[0] >= 60:
    print('best case')
    print(ll[0])
elif ll[-1] < 60:
    print(ll[-1])
    print('worst case')
else:
    for index, score in enumerate(ll):
        if score >= 60:
            print(ll[index-1])
            print(score)
            break
