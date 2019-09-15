'''
#0/1背包 #01背包 #動態規劃 #遞迴

INPUT:
6
10 8
25 25
65 75
25 29
25 17
15 20

OUTPUT:
112

'''


n = int(input())

#al 是體積列表 #bl 是飽足感列表
al = [0 for _ in range(n)]
bl = [0 for _ in range(n)]

for i in range(n):
    a, b = [int(x) for x in input().split()]
    al[i] = a
    bl[i] = b

def maxb(n, ta):
    '''
    #maxb 計算最大飽足感 #n 是飼料編號 #ta是剩餘體積 
    #https://zerojudge.tw/ShowProblem?problemid=d637
    # NA 30% 遞迴過深
    '''
    if n == 0:
        return 0
    if ta < al[n-1]:
        return maxb(n-1, ta)
    else:
        return max(maxb(n-1, ta-al[n-1]) + bl[n-1], maxb(n-1, ta))


def maxb_2(n, ta):
    '''
    #bottomup 用二維陣列紀錄

    '''
    costs = [[0 for _ in range(ta)] for _ in range(n)]
    pass

ans = maxb(n, 100)
print(ans)
