# b964: 第 1 題 成績指標
import sys
for n in sys.stdin:
    #ll = list(map(int, input().split()))
    ll = [int(x) for x in input().split()]
    ll.sort()
    #print(' '.join(list(map(str, ll))))
    print(*ll)
    if ll[0] >=60:
        print('best case')
        print(ll[0])
    elif ll[-1]<60:
        print(ll[-1])
        print('worst case')
    else:
        for index, score in enumerate(ll):
            if score >=60:
                print(ll[index-1])
                print(score)
                break
            
