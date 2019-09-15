#雙層迴圈 #forelse #for else #讀取數列

nums = map(int, input().split())

for num in nums:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")