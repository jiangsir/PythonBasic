#遞迴 #FIBONACCI #FIB

def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))


def fibDP(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

print(fibDP(10))
