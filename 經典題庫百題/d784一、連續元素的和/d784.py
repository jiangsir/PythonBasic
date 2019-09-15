
def e248_Greedy(nums):
    '''
    貪心法
    針對整個 list 尋找最大和
    可以不取某些數字
    Greedy 無法取得最大和
    '''
    import math
    sum = 0
    max = -math.inf
    for n in nums:
        sum += n
        if sum > max:
            max = sum
    return max

def d784_BF(nums):
    '''
    暴力法 O(n**3)
    '''
    import math
    max = -math.inf
    for L in range(len(nums)):
        for R in range(L, len(nums)):
            sum = 0
            for i in range(L, R+1):
                sum += nums[i]
            if sum > max:
                max = sum
    return max

import math
def d784_RC(L, R, nums):
    '''
    遞迴式
    if n==0: 0
    if n==1: nums[1]
    '''
    if L == R:
        if nums[L] > 0:
            return nums[L]
        else:
            return 0

    center = (L + R)//2
    Lmax = d784_RC(L, center, nums)
    Rmax = d784_RC(center+1, R, nums)

    lcentersum = 0
    lcentermax = -math.inf
    for i in range(L, center+1):
        lcentersum += i
        if lcentersum > lcentermax:
            lcentermax = lcentersum
    
    rcentersum = 0
    rcentermax = -math.inf
    for i in range(center+1, R+1):
        rcentersum += i
        if rcentersum > rcentermax:
            rcentermax = rcentersum

    return max(Lmax, Rmax, lcentermax+rcentermax)



def e248_DP():
    '''
    DP, O(nlogn)
    '''

# n = int(input())

# #print(e248_Greedy(nums))
# for i in range(n):
#     nums = [int(x) for x in input().split()]
#     #print("Greedy", e248_Greedy(nums[1:]))
#     #print("BF", d784_BF(nums[1:]))
#     print("RC", d784_RC(0, len(nums[1:]), nums[1:]))

n = int(input())
for i in range(n):
    nums = [int(x) for x in input().split()]
    nums = nums[1:]
    dp = [0 for _ in nums]

    dp[0] = nums[0]
    for i, num in enumerate(nums):
        if i > 0:
            dp[i] = max(num, num + dp[i-1])
    print(max(dp))
