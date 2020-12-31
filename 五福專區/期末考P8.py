n = int(input())
for i in range(n):
    nums = [int(x) for x in input().split()][1:]
    sums = [None for _ in nums]
    sums[0] = nums[0]
    for i in range(1, len(sums)):
        sums[i] = max(sums[i-1], 0) + nums[i]
    print(max(sums))

'''
3
5 1 2 -3 4 5
5 1 2 3 4 5
6 10 -5 7 6 -1 -3
'''