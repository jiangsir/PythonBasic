'''
#數列乘積 #數列相乘 #串列綜合表達式 #List Comprehension #解包

'''

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def solution1(l1, l2):
    l3 = [a*b for a, b in zip(l1, l2)]
    print(*l3)

    ans = 0
    for i in range(len(l1)):
        ans += l1[i] * l2[i]
    print(ans)

def solution2(l1, l2):
    l3 = [a*b for a, b in zip(l1, l2)]
    print(*l3)
    print(sum(l3))

def solution3(l1, l2):
    '''
    利用 reduce + lambda 來計算數列和
    '''
    import functools
    l3 = [a*b for a, b in zip(l1, l2)]
    print(*l3)

    ans = functools.reduce(lambda sum, elem: sum + elem, l3)
    print(ans)

solution1(l1, l2)
solution2(l1, l2)
solution3(l1, l2)
