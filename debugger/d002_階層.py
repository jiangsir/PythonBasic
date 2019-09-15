n = int(input())

for i in range(2, n):
	if n%i==0:
		print('非質數')
		break
else:
	print('質數')