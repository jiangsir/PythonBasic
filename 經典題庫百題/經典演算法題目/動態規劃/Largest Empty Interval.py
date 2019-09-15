# Largest Empty Interval #最長連續空格 #最長連續1

a = [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
# array[i]：障礙物為0，空白為1。

def longestRC(n):
    '''
    遞迴解法
    '''
    if n<0:
        return 0
    elif n==0:
        if a[n] == 0:
            return 0
        else:
            return 1
    else:
        if a[n] == 0:
            return 0
        else:
            return longestRC(n-1) + 1

print(longestRC(len(a)-1))


def longestDP(n, a):
    '''
    轉成 DP 解法
    '''
    dp = [0 for _ in a]
    if int(a[0]) == 0:
        dp[0] = 0
    else:
        dp[0] = 1
    
    for i in range(1, n+1):
        if int(a[i]) == 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + 1

    return max(dp)


a = input()
print(longestDP(len(a)-1, a))

assert 3 == longestDP(len(a)-1, a)

