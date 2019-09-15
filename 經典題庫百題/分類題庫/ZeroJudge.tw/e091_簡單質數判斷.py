# 迴圈 #迴圈中斷 #for else #forelse #質數

#n = 1000301
n = 999983

for i in range(2, n):
    if n%i==0:
        print('非質數')
        break
else:
    print("質數")