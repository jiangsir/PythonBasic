'''
https://zerojudge.tw/ShowProblem?problemid=b682

#時間計算 #餘數

'''

def solution1(h1, m1, h2, m2):
    m = ((h2-h1)%24*60+m2-m1)%(24*60)
    return m//60, m%60

def solution2(h1, m1, h2, m2):
    m = ((h2*60+m2) - (h1*60+m1))%(24*60)
    return m//60, m%60

h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())

#print(*solution1(h1, m1, h2, m2))
print(*solution2(h1, m1, h2, m2))
