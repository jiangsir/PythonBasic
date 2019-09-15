'''
https://zerojudge.tw/ShowProblem?problemid=b681

#數學式簡化 #True 可以為1計算 #布林轉整數 #取代 abs

'''

def solution1(L):
    if L>0:
        return L*2 -1
    else:
        return -L*2

def solution2(L):
    return abs(L)*2 - (L>0)

def solution3(L):
    return (L<0)*(-2*L) + (L>0)*(2*L-1)

L = int(input())

print(solution1(L))
print(solution2(L))
print(solution3(L))
