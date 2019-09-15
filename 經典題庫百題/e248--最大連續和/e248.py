
def e248_Greedy(nums):
    '''
    貪心法
    針對整個 list 尋找最大和
    可以不取某些數字
    '''
    sum = 0
    max = 0
    for n in nums:
        sum += n
        if sum <0:
            sum = 0
        if sum > max:
            max = sum
    return max



def e248_BF(nums):
    '''
    暴力法 O(n**3)
    '''
    max = 0
    for L in range(len(nums)):
        for R in range(L, len(nums)):
            sum = 0
            for i in range(L, R+1):
                sum += nums[i]
                if sum > max:
                    max = sum
    return max

def e248_DP():
    '''
    DP, O(nlogn)
    '''


nums = [1, 2, -6, 3, -2, 4, -1, 3, 2, -4]

#print(e248_Greedy(nums))

print(e248_BF(nums))
