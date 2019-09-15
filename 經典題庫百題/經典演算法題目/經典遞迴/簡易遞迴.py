'''
#簡易遞迴 
'''

nums = [3, 6, 88, 21, 56, 11, 45, 7]

def sum2(n):
    '''
    #數列連加也可以用遞迴寫出
    '''
    if n ==0:
        return 0
    else:
        return sum2(n-1) + nums[n-1]

def 連乘(n):
    ans = 1
    for num in nums:
        ans *= num
    return ans

def 連乘2(n):
    if n == 0:
        return 1
    else:
        return 連乘2(n-1) * nums[n-1]


def 香檳塔1():
    pass

def 香檳塔2():
    pass

def 香檳塔3():
    pass

def 圓形切割():
    pass

ans = sum(nums)
print(ans)

ans = sum2(len(nums))
print('sum2=', ans)

ans = 連乘(len(nums))
print('連乘=', ans)

ans = 連乘2(len(nums))
print('連乘2=', ans)