import math
'''
#http://www.csie.ntnu.edu.tw/~u91029/KnapsackProblem.html
#0/1 Knapsack Problem 
#0/1 背包 #遞迴 #組合最佳化

c() # 總價值
n：第0個到第n個物品要放進背包內。
w:  # 物品重量
weight[0~n-1]: #重量列表
cost[0~n-1]:   # 價值列表
c(n, w) = max( 放了 n, 不放 n )
        = max( c(n-1, w-weight[n])+cost[n], c(n-1, w) )


'''

#weight = [ 850, 300, 500, 200]
#cost = [ 400, 150, 150, 120]


# weight = [5, 4, 7, 2, 6]
# cost = [12, 3, 10, 3, 6]

# 資料來源: https://blog.csdn.net/weixin_39059738/article/details/79924049
cost = [2, 5, 3, 10, 4]
weight = [1, 3, 2, 6, 2]
items = [{cost: 2, weight: 1}, {cost: 5, weight: 3}, {
    cost: 3, weight: 2}, {cost: 10, weight: 6}, {cost: 4, weight: 2}]
n = 4
w = 11

cmatrix = [[None for _ in range(w)] for _ in range(n)]


def solution1_topdown(n, w):
    '''
    #topdown 遞迴 #邊遞迴邊紀錄
    # 邊遞迴邊紀錄是可以加快遞迴，但跟 bottomup 紀錄在二維陣列不同，
    # 裡面會留下很多 None 的紀錄，也就是遞會沒有經過的地方會留下 None
    None 2 2 None 2 2 None 2 2 None 0
    None None 5 None 7 None None None 7 None 7
    None None None None 8 None None None None None 10
    0 0 0 0 0 0 0 0 0 None 18
    '''
    if n == 0:
        cmatrix[n-1][w-1] = 0
        return cmatrix[n-1][w-1]

    if cmatrix[n-1][w-1] != None:
        return cmatrix[n-1][w-1]

    if w < weight[n-1]:  # 剩餘空間小於 n物件的重量，顯然只能選擇不放。
        cmatrix[n-1][w-1] = solution1_topdown(n-1, w)
        return cmatrix[n-1][w-1]
    else:
        cmatrix[n-1][w-1] = max(solution1_topdown(
            n-1, w-weight[n-1])+cost[n-1], solution1_topdown(n-1, w))
        return cmatrix[n-1][w-1]


def solution1():
    '''
    #遞迴 #topdown遞迴
    '''
    global cmatrix
    cmatrix = [[None for _ in range(w)] for _ in range(n)]

    ans = solution1_topdown(n, w)
    printMatrix(cmatrix)
    print('ans=', ans)


def solution2_buttomup(n, w):
    '''
    #用二維陣列紀錄 Buttomup #DP
    '''
    costmatrix = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j < weight[i]:
                costmatrix[i+1][j] = costmatrix[i][j]
            else:
                costmatrix[i+1][j] = max(costmatrix[i][j],
                                         costmatrix[i][j-weight[i]]+cost[i])
        print('solution2 i=', i)
        printMatrix(costmatrix)

    print('答案: ', costmatrix[n][w])


def solution2_bottomup2(n, w):
    '''
    #用一維陣列紀錄 Bottomup #DP
    '''
    costarray = [0 for _ in range(w+1)]
    for i in range(n):
        for j in range(w, 0, -1):
            if j >= weight[i]:
                costarray[j] = max(
                    costarray[j], costarray[j-weight[i]]+cost[i])
        print('costarray=', *costarray)
    print('最高價值=', costarray[w])


def printMatrix(matrix):
    for row in matrix:
        print(*row)


def solution2(n, w):
    '''
    #bottom up #由下往上 #DP #用二維陣列紀錄
    #用bottomup 紀錄則為了要能夠推演，每一格都會有紀錄
    '''
    printMatrix(cmatrix)


def solution3_force():
    '''
    #暴力法 
    '''
    pass


solution1()
solution2_buttomup(n, w)

solution2_bottomup2(n, w)
